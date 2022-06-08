from math import gcd

a = [list(map(int, input().split())) for _ in range(int(input()))]
a.append(a[0])
print(sum(gcd(abs(a[i][0] - a[i + 1][0]), abs(a[i][1] - a[i + 1][1])) for i in range(len(a) - 1)))
