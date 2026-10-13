#!/usr/bin/env python3
"""Repack only the verified A032M header-v2 layout; refuse AVB overlap."""
import hashlib
import json
import struct
import sys
from pathlib import Path


def pack(reference_path, kernel_path, dtb_path, output_path):
    reference = Path(reference_path).read_bytes()
    kernel, dtb = Path(kernel_path).read_bytes(), Path(dtb_path).read_bytes()
    assert reference[:8] == b'ANDROID!' and len(reference) == 67108864
    fields = struct.unpack_from('<10I', reference, 8)
    old_kernel_size, ramdisk_size, second_size = fields[0], fields[2], fields[4]
    page, version = fields[7:9]
    assert page == 2048 and version == 2 and second_size == 0
    recovery_size = struct.unpack_from('<I', reference, 1632)[0]
    assert recovery_size == 0
    align = lambda size: (size + page - 1) // page * page
    ramdisk_offset = page + align(old_kernel_size)
    ramdisk = reference[ramdisk_offset:ramdisk_offset + ramdisk_size]
    old_dtb_offset = ramdisk_offset + align(ramdisk_size)
    old_dtb_size = struct.unpack_from('<I', reference, 1648)[0]
    container = bytearray(reference[old_dtb_offset:old_dtb_offset + 64])
    magic, total, header_size, entry_size, entry_count = struct.unpack_from('>5I', container)
    assert magic == 0xd7b7ab1e and header_size == entry_size == 32
    assert entry_count == 1 and total == old_dtb_size
    assert struct.unpack_from('>I', container, 36)[0] == 64
    struct.pack_into('>I', container, 4, 64 + len(dtb))
    struct.pack_into('>I', container, 32, len(dtb))
    dt_container = bytes(container) + dtb
    assert reference[-64:-60] == b'AVBf'
    _, vbmeta_offset, vbmeta_size = struct.unpack_from('>3Q', reference, len(reference) - 52)
    new_ramdisk_offset = page + align(len(kernel))
    new_dtb_offset = new_ramdisk_offset + align(len(ramdisk))
    marker_offset = new_dtb_offset + align(len(dt_container))
    marker = b'SEANDROIDENFORCE'
    assert marker_offset + len(marker) <= vbmeta_offset, 'Candidate overlaps existing vbmeta'
    result = bytearray(reference)
    result[page:vbmeta_offset] = bytes(vbmeta_offset - page)
    result[page:page + len(kernel)] = kernel
    result[new_ramdisk_offset:new_ramdisk_offset + len(ramdisk)] = ramdisk
    result[new_dtb_offset:new_dtb_offset + len(dt_container)] = dt_container
    result[marker_offset:marker_offset + len(marker)] = marker
    struct.pack_into('<I', result, 8, len(kernel))
    struct.pack_into('<I', result, 1648, len(dt_container))
    struct.pack_into('>Q', result, len(result) - 52, marker_offset + len(marker))
    digest = hashlib.sha1()
    for component in (kernel, ramdisk, b'', b'', dt_container):
        digest.update(component)
        digest.update(struct.pack('<I', len(component)))
    result[576:608] = digest.digest() + bytes(12)
    assert result[vbmeta_offset:vbmeta_offset + vbmeta_size] == reference[vbmeta_offset:vbmeta_offset + vbmeta_size]
    assert result[new_ramdisk_offset:new_ramdisk_offset + len(ramdisk)] == ramdisk
    Path(output_path).write_bytes(result)
    return {'boot_size': len(result), 'kernel_size': len(kernel),
            'dtb_container_size': len(dt_container), 'header_version': version,
            'page_size': page, 'ramdisk_preserved': True, 'vbmeta_blob_preserved': True,
            'footer_original_image_size': marker_offset + len(marker),
            'sha256': hashlib.sha256(result).hexdigest(), 'hardware_tested': False,
            'avb_note': 'Existing signed descriptor already mismatches rooted payload. No valid new vendor signature claimed.'}


if __name__ == '__main__':
    print(json.dumps(pack(*sys.argv[1:]), indent=2))
