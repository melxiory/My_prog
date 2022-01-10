import sys

n = int(sys.stdin.readline())
parent = [int(i) for i in sys.stdin.readline().strip().split()]

list_a = [[] for _ in range(n + 1)]
for i in range(n):
  list_a[parent[i]] += [i]
r, l = list_a[-1], 0
while r:
  q, r = r, []
  for b in q:
    r += list_a[b]
  l += 1
print(l)
