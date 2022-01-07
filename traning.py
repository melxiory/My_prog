import sys, functools

list_A = str(sys.stdin.readline().strip())
list_B = str(sys.stdin.readline().strip())
def my_dist(a, b):
    @ functools.lru_cache(maxsize=len(a) * len(b))
    def recursive(i, j):
        if i == 0 or j == 0:
            return max(i, j)
        elif a[i - 1] == b[j - 1]:
            return recursive(i - 1, j - 1)
        else:
            return 1 + min(
                recursive(i, j - 1),
                recursive(i - 1, j),
                recursive(i - 1, j - 1)
            )
    return recursive(len(a), len(b))

print(my_dist(list_A, list_B))