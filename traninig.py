def increment_string(strng):
    if strng.isalpha():
        return strng + "1"
    if strng.isdigit():
        chislo = int(strng) + 1
        if len(str(strng)) > len(str(chislo)):
            return '0'*(len(str(strng)) - len(str(chislo))) + str(int(strng)+1)
        return str(int(strng)+1)
    if strng == '':
        return strng + "1"
    for i in range(len(strng)-1, -1, -1):
        if strng[i].isdigit() == False:
            strok = strng[i+1:]
            chislo = int(strok) + 1
            if len(strok) > len(str(chislo)):
                return strng[:i+1] + '0'*(len(strok)-len(str(chislo))) + str(chislo)
            else:
                return strng[:i+1] + str(chislo)




print(increment_string("foo"))
print(increment_string("foobar001"))
print(increment_string("foobar99"))
print(increment_string('000000000653431929'))

