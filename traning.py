import sys

n = int(sys.stdin.readline())
list_A = [int(i) for i in sys.stdin.readline().strip().split()]
list_B = [0] + [list_A[0]] + [False]*(n-1)
for i in range(1, len(list_A)):
    list_B[i+1] = max(list_B[i-1], list_B[i]) + list_A[i]
print(list_B[-1])