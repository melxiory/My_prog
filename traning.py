import sys

n = int(sys.stdin.readline())
list_A = [int(i) for i in sys.stdin.readline().strip().split()]
min_A = min(list_A)
k = (max(list_A) - min_A + 1)
list_B = [0] * k
for i in list_A:
    list_B[i - min_A] += 1
pos = 0
for j in range(0, k):
    for i in range(list_B[j]):
        list_A[pos] = str(j + min_A)
        pos += 1

print(' '.join(list_A))
