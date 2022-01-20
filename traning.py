import sys

sys.setrecursionlimit(10000)
n = int(sys.stdin.readline())
list_val1 = [[int(i) for i in sys.stdin.readline().strip().split()] for _ in range(n)]

T_F = [True]
acc = [float('-inf')]


class Catapult(Exception):
    pass

def in_order(i=0):
    if list_val1[i][1] == -1:
        if acc[0] > list_val1[i][0]:
            T_F[0] = False
            raise Catapult
        else:
            acc[0] = list_val1[i][0]
        if list_val1[i][2] != -1:
            in_order(list_val1[i][2])
        return
    in_order(list_val1[i][1])
    if acc[0] >= list_val1[i][0]:
        T_F[0] = False
        raise Catapult
    else:
        acc[0] = list_val1[i][0]
    if list_val1[i][2] != -1:
        in_order(list_val1[i][2])



if n == 0:
    print('CORRECT')
else:
    try:
        in_order()
        print('CORRECT')
    except Catapult:
        print('INCORRECT')
