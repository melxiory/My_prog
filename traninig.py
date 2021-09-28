from string import ascii_lowercase as abc, ascii_uppercase as ABC
from math import ceil

def _code(string, shift, mode):
    return ''.join(
        abc[(abc.index(c) + i*mode + shift) % len(abc)] if c in abc else
        ABC[(ABC.index(c) + i*mode + shift) % len(ABC)] if c in ABC else c
        for i, c in enumerate(string))

def moving_shift(string, shift):
    encoded = _code(string, shift, 1)
    cut = int(ceil(len(encoded) / 5.0))
    return [encoded[i : i+cut] for i in range(0, 5 * cut, cut)]

def demoving_shift(arr, shift):
    return _code(''.join(arr), -shift, -1)

print(moving_shift('os  afneewuftllzisohtj tbeca gikgeeeuiJ azxsoxaiOstaeaoemy eioecusdaorod eLiaaka', 13))
print(
    demoving_shift(moving_shift('os  afneewuftllzisohtj tbeca gikgeeeuiJ azxsoxaiOstaeaoemy eioecusdaorod eLiaaka', 13),
                   13))
