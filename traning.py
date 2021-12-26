import sys


def fetch_input():
    global v
    segments = []
    n, v = tuple([int(i) for i in sys.stdin.readline().strip().split()])
    for _ in range(n):
        segments.append(tuple([int(i) for i in sys.stdin.readline().strip().split()]))
    return segments


segments = fetch_input()
segments.sort(key=lambda x: x[0]/x[1])
segments.reverse()


def knap_sack(list_seg):
    list_rez = []
    for i in list_seg:
        if not list_rez:
            if v < i[1]:
                list_rez.append(i[0]*(v/i[1]))
                break
            else:
                list_rez.append(i[0])
                list_rez.append(i[1])
            if v == i[1]:
                list_rez.append(i[0])
                break
            continue
        if list_rez[1] + i[1] > v:
            list_rez[0] += i[0]*((v-list_rez[1])/i[1])
            break
        elif list_rez[1] + i[1] == v:
            list_rez[0] += i[0]
            break
        else:
            list_rez[0] += i[0]
            list_rez[1] += i[1]
    return f'{list_rez[0]:.3f}'


print(knap_sack(segments))
