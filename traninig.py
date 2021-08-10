import itertools


def slogan_maker(array):
    if not array: return []
    array_end = []
    for i in array:
        if i not in array_end:
            array_end.append(i)
    if len(array) == 1: return array
    spis_on_exit = []
    for i in itertools.permutations(array_end):
        spis_on_exit.append(i)
    return [' '.join(i) for i in spis_on_exit]


print(slogan_maker(["super"]))
print(slogan_maker(["super", "hot"]))
print(slogan_maker(["super", "hot", "guacamole"]))
print(slogan_maker(["super", "guacamole", "super", "super", "hot", "guacamole"]))
print(slogan_maker(["testing", "testing", "testing"]))
