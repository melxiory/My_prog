seq = [0, 1, 2, 2]


def find(n):
    if n not in seq:
        for i in range(n+1):
            if i not in seq:
                seq.extend([i]*seq[i])
        else:
            seq_count =[]
            count_seq = 2
            sum_count = 1
            for i in range(3, n+1):
                if seq.count(i) == count_seq:
                    sum_count += 1
                else:
                    seq_count.append([sum_count, count_seq])
                    count_seq += 1
                    sum_count = 1
            else:
                seq_count.append([sum_count, count_seq])
            return seq_count, seq.count(n)
    else:
        return seq.count(n) if n else 0


print(find(1000))
print(find(2000))
print(find(3000))
print(find(3))
print(find(4))
print(find(5))
