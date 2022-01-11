import sys

n = int(sys.stdin.readline())
packet = [tuple(int(i) if i.isdigit() else i for i in sys.stdin.readline().strip().split()) for _ in range(n)]
stack = []
stack_max = []
max_num = 0
for comm in packet:
    if comm[0] == 'push':
        stack.append(comm[1])
        if max_num < comm[1]:
            max_num = comm[1]
            stack_max.append(max_num)
        else:
            stack_max.append(max_num)
    if comm[0] == 'max':
        print(max_num)
    if comm[0] == 'pop' and stack:
        del stack[-1]
        del stack_max[-1]
        max_num = stack_max[-1] if stack_max else 0
