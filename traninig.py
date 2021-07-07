str = "A23456789TJQK"
card = "cdhs"

def encode(cards):
    return sorted([card.index(x[1]) * 13 + str.index(x[0]) for x in cards])

def decode(cards):
    return [f"{str[x % 13]}{card[x // 13]}" for x in sorted(cards)]


print(encode(["Td", "8c", "Ks"]))
print(encode(["Qh", "5h", "Ad"]))
print(encode(["8c", "Ks", "Td"]))
print(encode(["Qh", "Ad", "5h"]))

print(decode([7, 22, 51]))
print(decode([13, 30, 37]))
print(decode([7, 51, 22]))
print(decode([13, 37, 30]))