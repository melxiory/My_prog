def alphabet_war(battlefield):
    if '#' not in battlefield:
        return ''.join([i.lower() for i in battlefield if i.isalpha()])
    if battlefield.count('#') == 1:
        strok = ''
        for i in range(battlefield.count('[')):
            strok += battlefield[battlefield.index('[')+1:battlefield.index(']')]
            battlefield = battlefield[battlefield.index(']')+1:]
        return strok
    strok_1 =''
    for i in range(battlefield.count('[')):
        if battlefield[:battlefield.index('[')].count('#') == 2:
            battlefield = battlefield[battlefield.index(']')+1:]
        elif battlefield[:battlefield.index('[')].count('#') == 1:
            battlefield = battlefield[battlefield.index('[')+1:]
            if '[' in battlefield:
                if battlefield[:battlefield.index('[')].count('#') < 1:
                    strok_1 += battlefield[:battlefield.index(']')]
                else:
                    battlefield = battlefield[battlefield.index(']')+1:]
            else:
                if battlefield.count('#') < 1:
                    strok_1 += battlefield[:battlefield.index(']')]
                    return strok_1
                else:
                    return strok_1
        else:
            battlefield = battlefield[battlefield.index('[')+1:]
            if '[' in battlefield:
                if battlefield[:battlefield.index('[')].count('#') !=2:
                    strok_1 += battlefield[:battlefield.index(']')]
                    battlefield = battlefield[battlefield.index(']')+1:]
                else:
                    battlefield = battlefield[battlefield.index(']') + 1:]
            else:
                if battlefield.count('#') !=2:
                    strok_1 += battlefield[:battlefield.index(']')]
                    battlefield = battlefield[battlefield.index(']')+1:]
                else:
                    return strok_1
    return strok_1



print(alphabet_war('##abde[fgh]ijk[mn]op'))
print(alphabet_war('#abde[fgh]i#jk[mn]op'))
print(alphabet_war('[a][b][c]'))
print(alphabet_war('##a[a]b[c]#'))
