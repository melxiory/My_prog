def sum_array(a):
    return sum(a) if ''.join(str(i) for i in a).isdigit() else 0
print(sum_array([1.1, 2.2, 3.3]))

strok = ''.join(str(i if i == int else int(i)) for i in [1.1, 2.2, 3.3]).isdigit()
print(strok)