#!/usr/bin/env python3
"""Audit compiled FDT changes against the exact stock payload; no hardware claim."""
import json
import struct
import sys
from pathlib import Path


def properties(path):
    blob = Path(path).read_bytes()
    magic, size, off_struct, off_strings = struct.unpack_from('>4I', blob)
    assert magic == 0xd00dfeed and size == len(blob), 'Invalid FDT'
    result, stack, cursor = {}, [], off_struct
    while True:
        token = struct.unpack_from('>I', blob, cursor)[0]
        cursor += 4
        if token == 1:
            end = blob.index(0, cursor)
            stack.append(blob[cursor:end].decode())
            cursor = (end + 4) & ~3
        elif token == 2:
            stack.pop()
        elif token == 3:
            length, nameoff = struct.unpack_from('>2I', blob, cursor)
            cursor += 8
            name_start = off_strings + nameoff
            name = blob[name_start:blob.index(0, name_start)].decode()
            key = ('/' + '/'.join(stack[1:]), name)
            result[key] = blob[cursor:cursor + length]
            cursor = (cursor + length + 3) & ~3
        elif token == 4:
            continue
        elif token == 9:
            break
        else:
            raise ValueError(f'Invalid FDT token {token}')
    return result


def cells(value):
    assert len(value) % 4 == 0
    return list(struct.unpack('>' + 'I' * (len(value) // 4), value))


def audit(stock_path, candidate_path):
    stock, candidate = properties(stock_path), properties(candidate_path)
    changes = {key for key in stock.keys() | candidate.keys()
               if stock.get(key) != candidate.get(key)}
    gpu = '/soc/mm/gpu@60000000'
    expected = {
        ('/cpufreq-clus0', 'operating-points-2'): (1400000, 1150000),
        ('/cpufreq-clus1', 'operating-points-1'): (1800000, 1100000),
        ('/cpufreq-fcm', 'operating-points-1'): (1250000, 1100000),
    }
    allowed = set(expected) | {(gpu, name) for name in (
        'operating-points', 'sprd,dvfs-lists',
        'assigned-clocks', 'assigned-clock-rates')}
    assert changes == allowed, f'Unexpected FDT changes: {changes ^ allowed}'
    for key, top in expected.items():
        original, new = cells(stock[key]), cells(candidate[key])
        assert len(original) == len(new), 'DVFS index count changed'
        assert new[:2] == list(top) and new[2:] == original[2:]
        frequencies = new[::2]
        assert frequencies == sorted(set(frequencies), reverse=True)
        assert len(frequencies) <= 8, 'Hardware DVFS capacity exceeded'
    assert cells(candidate[(gpu, 'operating-points')]) == [256000, 0, 384000, 0, 600000, 0]
    assert cells(candidate[(gpu, 'sprd,dvfs-lists')]) == [256000, 0, 5, 1, 384000, 0, 7, 1, 600000, 0, 9, 1]
    clocks = cells(candidate[(gpu, 'clocks')])
    assigned = cells(candidate[(gpu, 'assigned-clocks')])
    assert assigned == clocks[18:20], 'GPU index 9 is not assigned GPLL'
    assert cells(candidate[(gpu, 'assigned-clock-rates')]) == [600000000]
    # All unlisted properties, including hot OPPs and thermal limits, matched.
    return {'changed_properties': sorted('/'.join(key) for key in changes),
            'hot_tables_preserved': True, 'dvfs_indices_preserved': True,
            'gpu_parent_mapping_validated': True, 'hardware_tested': False}


if __name__ == '__main__':
    print(json.dumps(audit(sys.argv[1], sys.argv[2]), indent=2))
