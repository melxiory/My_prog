import sys


def fetch_input():
    segments = []
    n = int(sys.stdin.readline())
    for _ in range(n):
        segments.append(tuple([int(i) for i in sys.stdin.readline().strip().split()]))
    return segments


segments = fetch_input()
segments.sort(key=lambda x: x[1])


def act_sel(list_seg):
    list_rez = []
    for i in list_seg:
        if not list_rez:
            list_rez.append(i)
            continue
        if i[0] <= list_rez[-1][1] <= i[1]:
            continue
        else:
            list_rez.append(i)
    list_rez = [i[1] for i in list_rez]
    return len(list_rez), list_rez


print(act_sel(segments))
