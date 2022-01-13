import sys

n = int(sys.stdin.readline())
list_heap = list(map(int, sys.stdin.readline().strip().split()))
list_swap = []

def sift_down(i):
    m_ind, l, r = i, 2 * i + 1, 2 * i + 2
    if l < n and list_heap[m_ind] > list_heap[l]:
        m_ind = l
    if r < n and list_heap[m_ind] > list_heap[r]:
        m_ind = r
    if i != m_ind:
        min_val = list_heap[i]
        list_heap[i] = list_heap[m_ind]
        list_heap[m_ind] = min_val
        list_swap.append([i, m_ind])
        sift_down(m_ind)


for l in range(n//2, -1, -1):
    sift_down(l)

print(len(list_swap))
for j in list_swap:
    print(*list(j))
