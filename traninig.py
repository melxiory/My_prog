class remember:
    def __init__(self, cls):
        self.cls = cls
        self.dict_state = {}

    def __call__(self, *args):
        args = args[0] if len(args) == 1 else args
        if args not in self.dict_state:
            if args and type(args) != int and len(args) == 2:
                x, y = args
                self.dict_state[args] = self.cls(x, y)
            elif not args:
                self.dict_state[args] = self.cls()
            else:
                self.dict_state[args] = self.cls(args)
        return self.dict_state[args]

    def __getitem__(self, item):
        return self.dict_state[item]

    def __iter__(self):
        return iter(self.dict_state)


@remember
class A(object):
    def __init__(self, x, y=0, z=0):
        pass


a = A(1)
b = A(2, 3)
c = A(4, 5, 6)
d = A(1)

print(A[1] is a is d)
print(A[2, 3] is b)
print(A[4, 5, 6] is c)
print({x for x in A})
"""
dict_state = {}
    def decor(*args):
        if args not in dict_state:
            dict_state[args] = args
        return dict_state[args]
"""