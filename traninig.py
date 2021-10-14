class Set:
    def __init__(self, value=[]):
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return 'Set:' + repr(self.data)

    def __iter__(self):
        return iter(self.data)


class MultiSet(Set):
    def intersect(self, *others):
        res = []
        for x in self:
            for other in others:
                if x not in other:
                    break
            else:
                res.append(x)
        return Set(res)

    def union(*args):
        res = []
        for seq in args:
            for x in seq:
                if not x in res:
                    res.append(x)
        return Set(res)


x = Set([1, 2, 3, 4])
y = Set([11, 12, 13, 14])
print(x | y)
print(x.intersect(y))
z = Set('front')
print(z[2])
for i in z:
    print(i)
print(z | 'back')
print(z & 'back')
X = MultiSet([1, 2, 4, 6, 8])
Y = MultiSet([1, 3, 5, 6, 8])
Z = MultiSet([2, 4, 6, 9, 10])
print(X|Y, Z|Y, Z|X)
print(X&Y, Z&Y, X&Z)
print(X.intersect(Y,Z))
print(X.union(Y,Z))
