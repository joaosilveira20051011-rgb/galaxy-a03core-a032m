#!/usr/bin/env python3
"""Compare AArch64 module CRCs and vermagic without loading or modifying them."""
import hashlib
import json
import struct
import sys
from pathlib import Path


def sections(path):
    blob = path.read_bytes()
    assert blob[:6] == b'\x7fELF\x02\x01', 'Expected ELF64 little-endian'
    assert struct.unpack_from('<H', blob, 18)[0] == 183, 'Expected AArch64'
    offset = struct.unpack_from('<Q', blob, 40)[0]
    entry_size, count, names_index = struct.unpack_from('<3H', blob, 58)
    assert entry_size == 64
    headers = [struct.unpack_from('<IIQQQQIIQQ', blob, offset + i * 64)
               for i in range(count)]
    header = headers[names_index]
    names = blob[header[4]:header[4] + header[5]]
    return {names[h[0]:].split(b'\0', 1)[0].decode():
            blob[h[4]:h[4] + h[5]] for h in headers if h[1] != 8}


def audit(symvers, module_paths, expected_release):
    symbols = {}
    for line in Path(symvers).read_text().splitlines():
        fields = line.split()
        if len(fields) >= 2:
            symbols[fields[1]] = int(fields[0], 16)
    results = []
    for path in sorted(module_paths):
        content = sections(path)
        versions = content['__versions']
        assert len(versions) % 64 == 0
        missing, mismatches = [], []
        for offset in range(0, len(versions), 64):
            crc = struct.unpack_from('<Q', versions, offset)[0]
            name = versions[offset + 8:offset + 64].split(b'\0', 1)[0].decode()
            if name not in symbols:
                missing.append(name)
            elif crc != symbols[name]:
                mismatches.append({'symbol': name, 'module_crc': hex(crc),
                                   'kernel_crc': hex(symbols[name])})
        info = content['.modinfo'].split(b'\0')
        vermagic = next(value.decode().split('=', 1)[1]
                        for value in info if value.startswith(b'vermagic='))
        assert vermagic.split()[0] == expected_release, f'{path.name}: release mismatch'
        results.append({'module': path.name, 'imports': len(versions) // 64,
                        'mismatches': mismatches, 'missing': missing,
                        'vermagic': vermagic,
                        'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    report = {'module_count': len(results),
              'import_entries_checked': sum(result['imports'] for result in results),
              'hardware_loading_tested': False, 'results': results}
    print(json.dumps(report, indent=2))
    return 1 if any(result['missing'] or result['mismatches'] for result in results) else 0


if __name__ == '__main__':
    paths = [path for directory in sys.argv[3:] for path in Path(directory).glob('*.ko')]
    assert paths, 'No modules supplied'
    sys.exit(audit(sys.argv[1], paths, sys.argv[2]))
