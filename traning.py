alph = [*map(chr, range(0x1F600, 0x1F64F + 1))]
def _code(string, shift):
    return ''.join(
        alph[(alph.index(c) + shift) % len(alph)] if c in alph else c
        for i, c in enumerate(string))

def moving_shift(string, shift):
    encoded = _code(string, shift)
    return encoded


print(moving_shift('😀🙏😇', 1))