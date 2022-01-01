import sys

n = list(map(int, sys.stdin.readline().strip().split()))[1:]
k = list(map(int, sys.stdin.readline().strip().split()))[1:]

for i in k:
    l, r = 0, len(n) - 1
    while l <= r:
        m = (l + r) // 2
        if n[m] == i:
            rez = m+1
            break
        if n[m] > i:
            r = m - 1
        else:
            l = m + 1
    else:
        rez = -1
    print(rez)
