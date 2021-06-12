def expanded_form(num):
    strok = ''
    for i in range(len(str(num))):
        if i != (len(str(num))-1):
            if str(num)[i] != '0':
                strok += str(num)[i] + '0'*(len(str(num))-1-i) + ' + '
        else:
            if str(num)[i] != '0':
                strok += str(num)[i]
            else:
                strok = strok[:len(strok)-3]
    return strok

print(expanded_form(9000000))
print(expanded_form(626950))
print(expanded_form(70304))
