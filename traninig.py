from itertools import combinations_with_replacement

def find_all(sum_dig, digs):
    combs = combinations_with_replacement(list(range(1, 10)), digs)
    target = [''.join(str (x) for x in list(comb)) for comb in combs if sum(comb) == sum_dig]
    if not target:
        return []
    return [len(target), int(target[0]), int(target[-1])]





print(find_all(10, 3))
print(find_all(27, 3))
print(find_all(84, 4))
print(find_all(35, 6))