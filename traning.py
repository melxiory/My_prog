import json
js = json.loads(input())
dict_par = {}
dict_numb = {}
def search_par(name):
    for j in js:
        if name == j['name']:
            lst = []
            for par in j['parents']:
                lst += [par]
                lst += search_par(par)
            return lst

for i in js:
    name = i['name']
    dict_par[name] = list(set(search_par(name)))
for k in dict_par:
    dict_numb[k] = 1
    for n in dict_par.values():
        if k in n:
            dict_numb[k] += 1
for i in sorted(list(dict_numb.items())):
    print(i[0], ':', i[1])


