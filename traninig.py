def closest(strng):
    if not strng:
        return []
    spisok = sorted([[sum(map(int, i)), j, int(i)] for j, i in enumerate(strng.split())])
    spisok_vix = [spisok[0], spisok[1]]
    for i in range(1, len(spisok)-1):
        if spisok[i+1][0]-spisok[i][0] < spisok_vix[1][0]-spisok_vix[0][0]:
            spisok_vix = [spisok[i], spisok[i+1]]
    return spisok_vix


print(closest("103 123 4444 99 2000"))
print(closest("456899 50 11992 176 272293 163 389128 96 290193 85 52"))
print(closest("239382 162 254765 182 485944 134 468751 62 49780 108 54"))
print(closest("241259 154 155206 194 180502 147 300751 200 406683 37 57"))
print(closest("89998 187 126159 175 338292 89 39962 145 394230 167 1"))
