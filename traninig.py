n = int(input())
ld = {i ** 2 + u ** 2: [i, u] for i in range(int(n ** 0.5) + 1) for u in range(i, int(n ** 0.5) + 1)}
for i in ld:
    if n - i in ld:
        print(*list(filter(lambda x: x, ld[i] + ld[n - i]))[::-1], sep=' ')
        break