import sys

n = int(sys.stdin.readline())
list_val1 = [[int(i) for i in sys.stdin.readline().strip().split()] for _ in range(n)]


def in_order(i=0):
    if list_val1[i][1] == -1:
        print(list_val1[i][0], end=' ')
        if list_val1[i][2] != -1:
            in_order(list_val1[i][2])
        return
    in_order(list_val1[i][1])
    print(list_val1[i][0], end=' ')
    if list_val1[i][2] != -1:
        in_order(list_val1[i][2])


def pre_order(i=0):
    if list_val1[i][1] == -1:
        print(list_val1[i][0], end=' ')
        if list_val1[i][2] != -1:
            pre_order(list_val1[i][2])
        return
    print(list_val1[i][0], end=' ')
    pre_order(list_val1[i][1])
    if list_val1[i][2] != -1:
        pre_order(list_val1[i][2])


def post_order(i=0):
    if list_val1[i][1] == -1:
        if list_val1[i][2] != -1:
            post_order(list_val1[i][2])
            print(list_val1[i][0], end=' ')
        else:
            print(list_val1[i][0], end=' ')
        return
    post_order(list_val1[i][1])
    if list_val1[i][2] != -1:
        post_order(list_val1[i][2])
    print(list_val1[i][0], end=' ')


in_order()
print()
pre_order()
print()
post_order()
