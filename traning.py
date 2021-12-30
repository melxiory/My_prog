import heapq

n = int(input())
list_comm = [i for i in [input().split() for _ in range(n)]]
list_heap = []



for i in list_comm:
    if i[0] == 'Insert':
        heapq.heappush(list_heap, int(i[1])*(-1))
    if i[0] == 'ExtractMax':
        print(heapq.heappop(list_heap)*(-1))
