import sys

n, e, d = list(map(int, sys.stdin.readline().strip().split()))
list_val1 = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(e)]
list_val2 = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(d)]


class Mergerset():
    def __init__(self):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, i):
        while i != self.parents[i]:
            i = self.parents[i]
        return i

    def union(self, i, j):
        i_id, j_id = self.find(i - 1), self.find(j - 1)
        if i_id == j_id: return
        if self.rank[i_id] > self.rank[j_id]:
            self.parents[j_id] = i_id
        else:
            self.parents[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1

    def union_2(self, i, j):
        if self.parents[self.find(i - 1)] == self.parents[self.find(j - 1)]:
            return 0


q = Mergerset()
for l in list_val1:
    q.union(*l)
for j in list_val2:
    if q.union_2(*j) == 0:
        print(0)
        break
else:
    print(1)
