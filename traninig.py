n = int(input())
t = [[9] * n for i in range(n)]
i, j, k, l = 0, 0, 1, 0
for _ in range(n * n):
    t[i][j] = k
    if i <= j + 1 and i + j < n - 1:
        j += 1
    elif i < j and i + j >= n - 1:
        i += 1
    elif i >= j and i + j > n - 1:
        j -= 1
    elif i > j + 1 and i + j <= n - 1:
        i -= 1
    if i-1 >= 0 and j == l and k == t[i-1][j]:
        k = 0 if k else 1
        l += 1
for q in t:
    print(*q)
