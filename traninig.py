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

def balanced_parens(n):
    return [s for s in paren(n)]


print(balanced_parens(0))
print(balanced_parens(2))
print(balanced_parens(3))
print(balanced_parens(4))
