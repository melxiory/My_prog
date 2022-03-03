dct_cls = {i[0]: i[1:] if len(i) > 1 else [] for i in
           [[i for i in input().split() if i.isalpha()] for _ in range(int(input()))]}
lst_req = [input() for _ in range(int(input()))]
stack = []
dct_er = {i: set() for i in dct_cls}
for i in dct_cls:
    for q, r in dct_cls.items():
        if i in r:
            dct_er[i].add(q)
            if dct_cls[i]:
                dct_er[i].add(q)
r = 0
for j in lst_req:
    if j in stack:
        print(j)
    elif j in dct_er:
        stack.append(j)
        while r < len(stack):
            for q in dct_er.get(stack[r], ''):
                if q not in stack:
                    stack.append(q)
            r += 1





parents = {}
for _ in range(int(input())):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]

def is_parent(child, parent):
    if child == parent: return True
    for p in parents[child]:
        if is_parent(p, parent ): return True
    return False

exceptions = []
for _ in range(int(input())):
    a = input().strip()
    for i in exceptions:
        if is_parent(a,i):
            print(a)
            break
    exceptions.append(a)