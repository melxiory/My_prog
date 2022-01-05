import sys

n = int(sys.stdin.readline())
list_A = [int(i) for i in sys.stdin.readline().strip().split()]
list_B = [0 for i in range(n+1)]
for i in range(n):
    list_B[i] = 1
    for j in range(i):
        if list_A[i] % list_A[j] == 0 and list_B[j] + 1 > list_B[i]:
            list_B[i] += 1
print(max(list_B))