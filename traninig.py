def power_sumDigTerm(n):
    power_sum = []
    for i in range(2, 100):
        for j in range(2, 50):
            pow_i = i ** j
            if sum(map(int, str(pow_i))) == i:
                power_sum.append(pow_i)
    power_sum.sort()
    return power_sum[n-1]


print(power_sumDigTerm(1))
print(power_sumDigTerm(2))
print(power_sumDigTerm(3))
print(power_sumDigTerm(4))
print(power_sumDigTerm(6))
print(power_sumDigTerm(7))
print(power_sumDigTerm(8))
print(power_sumDigTerm(9))
print(power_sumDigTerm(10))
print(power_sumDigTerm(11))