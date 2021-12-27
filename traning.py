import sys

n = int(sys.stdin.readline())


def var_terms(n):
    if n == 1:
        return [1]
    if n == 2:
        return [2]
    list_term = [1]
    sum_terms = 1
    for i in range(2, n + 1):
        if sum_terms + i + i + 1 <= n:
            sum_terms += i
            list_term.append(i)
            continue
        elif sum_terms + i == n:
            sum_terms += i
            list_term.append(i)
            break
    return list_term


print(var_terms(n))
