import sys

n = int(sys.stdin.readline())
list_A = [int(i) for i in sys.stdin.readline().strip().split()]
inf = -10**10
list_B = [-inf] + [inf] * (n + 1)
prev = []
for i in range(n):
    left = 0
    right = n + 1
    while left + 1 < right:
        middle = (left + right) // 2
        if list_B[middle] >= list_A[i]:
            left = middle
        else:
            right = middle
    list_B[right] = list_A[i]
    prev.append([right, i, list_A[i]])
z = n+1
while list_B[z] == inf:
    z -= 1
prev.reverse()
result = []
for i in prev:
    if i[0] == z:
        result.append(str(i[1]+1))
        z -= 1
result.reverse()
print(len(result))
print(' '.join(result))



'''
list_B = [0 for i in range(n)]
for i in range(n):
    list_B[i] = 1
    for j in range(i):
        if list_A[i] <= list_A[j] and list_B[j] + 1 > list_B[i]:
            list_B[i] += 1
k = max(list_B)
list_rez = [0 for i in range(k)]
ind = list_B.index(k)
list_rez[-1] = ind+1
r, q = k, k-1
for l in range(ind - 1, -1, -1):
    if list_A[l] >= list_A[list_rez[q]-1] and list_B[l]+1 == r:
        q -= 1
        list_rez[q] = l+1
        r -= 1
list_rez = [str(i) for i in list_rez if i !=0]
print(k)
print(' '.join(list_rez))
'''
