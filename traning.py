import sys

r = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()[:n]))

revers = 0


def merge(i, j):
    global revers
    Q = [0]
    while i or j:
        if not i:
            Q += j
            break
        if not j:
            Q += i
            break
        if i[0] > j[0]:
            Q += [j[0]]
            revers += len(i)
            del j[0]
        else:
            Q += [i[0]]
            del i[0]
    del Q[0]
    return Q


def merge_sort(spis):
    dlin = len(spis)
    if dlin > 1:
        m = dlin // 2
        return merge(merge_sort(spis[:m + 1 if dlin > 2 and dlin % 2 else m]),
                     merge_sort(spis[m + 1 if dlin > 2 and dlin % 2 else m:]))
    else:
        return spis


merge_sort(A)
print(revers)
