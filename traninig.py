def is_prime(num):
    prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
    i = 5;
    d = 2;

    while prime and i * i <= num:
        prime = num % i != 0
        i += d
        d = 6 - d
    return prime

n = int(input())
if is_prime(n):
    print("YES")
else:
    print("NO")