dct_cls = {i[0]: i[1:] if len(i) > 1 else [] for i in
           [[i for i in input().split() if i.isalpha()] for _ in range(int(input()))]}
lst_req = [input().split() for _ in range(int(input()))]
for j in lst_req:
    if len(j) > 1 and j[1] in dct_cls:
        stack, r = dct_cls[j[1]], 0
        while r < len(stack):
            if j[0] in stack or j[0] == j[1]:
                print('Yes')
                break
            else:
                for q in dct_cls.get(stack[r], ''):
                    if q not in stack:
                        stack.append(q)
                r += 1
        else:
            if j[0] == j[1] and j[0] in dct_cls:
                print('Yes')
            else:
                print('No')
    else:
        print('No')