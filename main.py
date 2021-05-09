from random import randint

spisok = []

for i in range(10):
    spisok.append(randint(1, 9))

b = 154

print(spisok+[22, 22, 22], b)

spisok.pop()