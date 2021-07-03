def valid(a):
    dlin1 = len(a[0])
    dlin2 = len(a[0][0])
    kol_players = ''.join(a[0])
    if len(a[0][0]) % 2 == 1:
        return False
    for i in a:
        if len(i) != dlin1:
            return False
        for j in i:
            if len(j) != dlin2:
                return False
            for l in j:
                if l not in kol_players:
                    return False
    spis_nach = [j for i in a for j in i]
    spis = []
    if len(a[0][0]) == 4:
        for i in spis_nach:
            for j in range(3):
                spis.append(i[j]+i[j+1])
    for i in spis:
        if spis.count(i) >= 1 and spis.count(i[1]+i[0]) >= 1 or spis.count(i) > 1:
            return False
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

