import sys


def fetch_input():
    segments = []
    n = tuple([int(i) for i in sys.stdin.readline().strip().split()])[0]
    for _ in range(n):
        segments.append(tuple([i for i in sys.stdin.readline().strip().split(':')]))
    segments = {j.strip(): i for i, j in segments}
    cod_1 = sys.stdin.readline()
    return segments, cod_1[:len(cod_1) - 1]


segments = fetch_input()


def huffman_decode(seg):
    dict_dec, code = seg
    dict_rez = []
    summator = 0
    while code:
        if code[:summator] in dict_dec:
            dict_rez.append(dict_dec[code[:summator]])
            code = code[summator:]
            summator = 0
        else:
            summator += 1
    return ''.join(dict_rez)


def main():
    rez = huffman_decode(segments)
    print(rez)


main()
