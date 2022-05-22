n, m = map(int, input().split())
a = [[0] * m for i in range(n)]
s = 0
for k in range(n + m + 1):
    for i in range(n):
        for j in range(m):
            if i + j + 1 == k:
                a[i][j] = f'{s:>3}'
                s += 1
[print(*_, sep='') for _ in a]
