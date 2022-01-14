import sys, queue

n, m = list(map(int, sys.stdin.readline().strip().split()))
list_heap = list(map(int, sys.stdin.readline().strip().split()))
q = queue.PriorityQueue(maxsize=n)
acc = 0
for i in list_heap:
    if q.full():
        rez = q.get()
        acc = rez[1]
        print(rez[1], rez[0])
        q.put((rez[0] + i, acc))
        acc += 1
    else:
        if i == 0:
            print(acc, 0)
            continue
        print(acc, 0)
        q.put((i, acc))
        acc += 1
