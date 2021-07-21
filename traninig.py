def alphabet_war(battlefield):
    if '#' not in battlefield:
        return battlefield.replace('[', '').replace(']', '')
    sectors = [sep for bunker in battlefield.split('[') for sep in bunker.split(']')]
    fields = sectors[0::2]
    bunkers = sectors[1::2]
    return ''.join(b for i, b in enumerate(bunkers) if ''.join(fields[i:i+2]).count('#') < 2)


print(alphabet_war('##abde[fgh]ijk[mn]op'))
print(alphabet_war('#abde[fgh]i#jk[mn]op'))
print(alphabet_war('[a][b][c]'))
print(alphabet_war('##a[a]b[c]#'))
