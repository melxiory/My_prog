def valid(a):
    d = {}
    day_length = len(a[0])
    group_size = len(a[0][0])
    golfers = {g for p in a[0] for g in p}

    for day in a:
        if len(day) != day_length: return False
        for group in day:
            if len(group) != group_size: return False
            for player in group:
                if player not in golfers: return False
                if player not in d:
                    d[player] = set(group)
                else:
                    if len(d[player] & set(group)) > 1:
                        return False
                    else:
                        d[player].add(group)
    return True

print(valid([['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'], ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'], ['AGKO', 'BIPT', 'CJMS', 'DHFR', 'ELNQ'], ['AHLP', 'NKBS', 'CEOR', 'DFIQ', 'MJGT'], ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']]))
print(valid([ ["AB"] ]))
print(valid([
    ["AB", "CD"],
    ["AD", "BC"],
    ["BD", "AC"]]))
print(valid([
    ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
    ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
    ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
    ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
    ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']]))
print(valid([
    ["AB", "CD", "EF", "GH"],
    ["AC", "BD", "EG", "FH"],
    ["AD", "CE"],
    ["AE", "BG", "CH", "FD"]]))

