def paren(left, right=None):
    if right is None:
        right = left  # allows calls with one argument

    if left == right == 0: # base case
        yield ""

    else:
        if left > 0:
            for p in paren(left-1, right): # first recursion
                yield "("+p

        if right > left:
            for p in paren(left, right-1): # second recursion
                yield ")"+p

def balanced_parens(n, k):
    parens = []
    for i in paren(n):
        parens.append(i)
        if len(parens) > k:
            break
    return parens[k] if len(parens) > k > -1 else None


print(balanced_parens(0, 0))
print(balanced_parens(1, 0))
print(balanced_parens(2, 0))
print(balanced_parens(3, 5))
print(balanced_parens(3, -1))
