n, m = map(int, input().split())
x = [tuple(map(int, input().split())) for _ in range(int(input()))]
f = [[(0, '*')[(r + 1, c + 1) in x] for c in range(m)] for r in range(n)]
for r in range(n):
    for c in range(m):
        if f[r][c] != '*':
            f[r][c] = sum(f[i][j] == '*' for i in range(max(0, r - 1), min(r + 2, n)) 
                                         for j in range(max(0, c - 1), min(c + 2, m)))            
[print(*_) for _ in f]