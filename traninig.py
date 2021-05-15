def digitize(n):
    return [int(i) for i in list(str(n))[::-1]  ]

print(digitize(23423))