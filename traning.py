import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))
table_size = list(map(int, sys.stdin.readline().strip().split()))
dest_sour = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]


class Mergerset():
    def __init__(self, lst):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
        self.max = max(lst)

    def find(self, i):
        while i != self.parents[i]:
            i = self.parents[i]
        return i

    def union(self, i, j):
        i_id, j_id = self.find(i - 1), self.find(j - 1)
        if i_id == j_id: return
        if self.rank[i_id] > self.rank[j_id]:
            self.parents[j_id] = i_id
            table_size[i_id] += table_size[j_id]
            self.max = table_size[i_id] if self.max < table_size[i_id] else self.max
        else:
            self.parents[i_id] = j_id
            table_size[j_id] += table_size[i_id]
            self.max = table_size[j_id] if self.max < table_size[j_id] else self.max
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1

    def get_max(self):
        print(self.max)


q = Mergerset(table_size)
for l in dest_sour:
    q.union(*l)
    q.get_max()

'''
max_val = max(table_size)
for i, j in dest_sour:
    if i == j or type(table_size[i - 1]) == str and int(table_size[i - 1][-2]) == j-1 or type(table_size[j - 1]) == str and int(table_size[j - 1][-2]) == i-1:
        print(max_val)
        continue
    if type(table_size[i - 1]) == str and type(table_size[j - 1]) == str:
        table_size[int(table_size[i - 1][-2])] += eval(table_size[j - 1])
        table_size[int(table_size[j - 1][-2])] = table_size[int(table_size[i - 1][-2])]
        if table_size[int(table_size[i - 1][-2])] > max_val:
            max_val = table_size[int(table_size[i - 1][-2])]
    elif type(table_size[i - 1]) == str:
        table_size[int(table_size[i - 1][-2])] += table_size[j - 1]
        table_size[j - 1] = table_size[i - 1]
        if table_size[int(table_size[i - 1][-2])] > max_val:
            max_val = table_size[int(table_size[i - 1][-2])]
    elif type(table_size[j - 1]) == str:
        table_size[int(table_size[j - 1][-2])] += table_size[i - 1]
        table_size[i - 1] = table_size[j - 1]
        if table_size[int(table_size[j - 1][-2])] > max_val:
            max_val = table_size[int(table_size[i - 1][-2])]
    else:
        table_size[i - 1] += table_size[j - 1]
        table_size[j - 1] = f'table_size[{i-1}]'
        if table_size[i - 1] > max_val:
            max_val = table_size[i - 1]
    print(max_val)

'''
