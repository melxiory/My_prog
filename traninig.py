def exp_sum(n):
    dic = {}

    def p(n, k):
        if n < k:
            return 0
        if n == k:
            return 1
        if k == 0:
            return 0

        key = str(n) + ',' + str(k)
        try:
            temp = dic[key]
        except:
            temp = p(n - 1, k - 1) + p(n - k, k)
            dic[key] = temp
        finally:
            return temp

    partitions_count = 0

    for k in range(n + 1):
        partitions_count += p(n, k)
    return partitions_count


print(exp_sum(1))
print(exp_sum(2))
print(exp_sum(3))
print(exp_sum(4))
print(exp_sum(5))
print(exp_sum(10))
