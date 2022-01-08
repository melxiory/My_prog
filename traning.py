import sys

W, n = [int(i) for i in sys.stdin.readline().strip().split()]
list_W = [int(i) for i in sys.stdin.readline().strip().split()]
H = [1] + [0]*W
for i in range(n):
    for j in range(W, list_W[i] - 1, -1):
        if H[j - list_W[i]] == 1:
            H[j] = 1
while H[W] == 0:
    W -= 1
print(W)