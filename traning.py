import sys

size, n = tuple(int(i) for i in sys.stdin.readline().strip().split())
packet = [tuple(int(i) for i in sys.stdin.readline().strip().split()) for _ in range(n)]
t_end, len_turn, sm = 0, 0, 1
list_turn = []
for i, (t_a, t_d) in enumerate(packet):
    if not list_turn:
        list_turn.append(t_a)
        t_end, len_turn = t_a + t_d, len_turn+1
        continue
    if len_turn < size and t_a <= t_end:
        list_turn.append(t_end)
        t_end += t_d
        len_turn += 1
    elif t_a < t_end and len_turn == size:
        if size < 2:
            list_turn.append(-1)
        elif list_turn[i-len_turn+sm] <= t_a:
            list_turn.append(t_end)
            t_end += t_d
        else:
            list_turn.append(-1)
            sm -= 1
    elif t_a >= t_end:
        list_turn.append(t_a)
        t_end, len_turn, sm = t_a + t_d, 1, 1

for i in list_turn:
    print(i)