import random as rnd

rnd.seed(42)
clear_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = 6
text = 'Some encripted text'


def caesar(text, key, alphabet):
    return alphabet[(alphabet.index(text) + key) % len(alphabet)]


def jarriquez_encryption(text, key, alphabet, reverse=False):
    if not reverse:
        return caesar(text, int(key), alphabet)
    else:
        return caesar(text, -int(key), alphabet)



def disc_generator(alphabet):
    lst = list(alphabet)
    random.shuffle(lst)
    return ''.join(lst)


discs = [disc_generator(clear_alphabet) for _ in range(n)]


def jefferson_encryption(text, discs, step, reverse=False):
    t = [i.upper() for i in text if i.isalnum()]
    n, st = 0, ''
    for j in t:
        if n == len(discs):
            n = 0
        st += jarriquez_encryption(j, step, discs[n], reverse)
        n += 1
    return st


print(jefferson_encryption(text, discs, 13))
