def wave(people):
    spisok = []
    for i in range(len(people)):
        if 0 < i < len(people)-1:
            if people[i] != ' ':
                spisok.append(people[:i] + people.upper()[i] + people[i+1:])
        elif i == 0:
            if people[i] != ' ':
                spisok.append(people.upper()[0] + people[1:])
        else:
            if people[i] != ' ':
                spisok.append(people[:i] + people.upper()[i])
    return spisok

print(wave("hello"))
