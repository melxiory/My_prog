import requests as req, re
a = input()
res = req.get(a)
lst_dom = []
for i in re.findall(r'<\w .*href=(.http://|.https://|.ftp://|\'|\")(.+?[\.](\w\w|\w\w\w))[^\.\w\d]', res.text):
    if i[1] not in lst_dom:
        lst_dom.append(i[1])
else:
    lst_dom.sort()
    print(*lst_dom, sep='\n')
