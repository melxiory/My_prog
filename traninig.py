def kebabize(string):
    return ''.join(['-'+i if j!=0 and i.isupper() else i for j, i in enumerate(string) if i.isalpha()]).lower()


print(kebabize('myCamelCasedString'))
print(kebabize('myCamelHas3Humps'))
print(kebabize('SOS'))
print(kebabize('42'))