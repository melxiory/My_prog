def is_alpha(strok):
    return ''.join([i for i in strok if i in 'qwertyuiopasdfghjklzxcvbnm'])


def is_digit(strok):
    strok_digit = ''.join([i for i in strok if i in '+-1234567890'])
    if strok_digit == '-':
        strok_digit = strok_digit + '1'
    if strok_digit == '+':
        strok_digit = '1'
    if strok_digit == '':
        strok_digit = '1'
    return int(strok_digit)


def simplify(poly):
    list_replace = poly.replace('-', ' -').replace('+', ' +')
    list_split = list_replace.split()
    list_sort = [str(''.join(sorted(i))) for i in list_split]
    list_sorted = sorted(list_sort, key=lambda strok: ((len(is_alpha(strok))),
                                                       is_alpha(strok)[0], is_alpha(strok)[1] if len(is_alpha(strok)) > 1 else [0]))
    final_result = ''
    while list_sorted:
        iterium_relust = list_sorted.pop(0)
        for i in list_sorted.copy():
            if is_alpha(iterium_relust) == is_alpha(i):
                iterium_relust = str(is_digit(iterium_relust) + is_digit(i)) + is_alpha(iterium_relust)
                list_sorted.pop(list_sorted.index(i))
                if iterium_relust[0] == '0' or iterium_relust[1] == '0':
                    break
        else:
            if iterium_relust[0] == '1' and is_digit(iterium_relust) == 1:
                iterium_relust = iterium_relust[1:]
            if len(iterium_relust) > 1 and  iterium_relust[1] == '1' and is_digit(iterium_relust) == 1:
                iterium_relust = iterium_relust[0] + iterium_relust[2:]
            if iterium_relust[0] != '+' and iterium_relust[0] != '-':
                iterium_relust = '+' + iterium_relust
            final_result = final_result + iterium_relust
    return final_result[1:] if final_result[0] == '+' else final_result



print(simplify("dc+dcba"))
print(simplify("2xy-yx"))
print(simplify("-a+5ab+3a-c-2a"))
print(simplify("-abc+3a+2ac"))
print(simplify("xyz-xz"))
print(simplify("a+ca-ab"))
print(simplify("xzy+zby"))
