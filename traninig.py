def find_all(sum_dig, digs):
    def _part(n, k, pre):
        if n <= 0:
            return []
        if k == 1:
            if n <= pre:
                return [[n]]
            return []
        ret = []
        for i in range(min(pre, n), 0, -1):
            if len(str(i)) == 1:
                ret += [[i] + sub for sub in _part(n-i, k-1, i)]
        return ret
    list_dig = sorted(map(sorted, _part(sum_dig, digs, sum_dig)))
    return [len(list_dig), int(''.join(map(str, list_dig[0]))), int(''.join(map(str, list_dig[len(list_dig)-1])))] if list_dig else []





print(find_all(10, 3))
print(find_all(27, 3))
print(find_all(84, 4))
print(find_all(35, 6))