def encode(cards):
    dict_mast = {values: key for key, values in enumerate([x + y for y in ['c', 'd', 'h', 's']
                                                           for x in
                                                           ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q',
                                                            'K']])}
    spis_encode = sorted([dict_mast[i] for i in cards])
    return spis_encode


def decode(cards):
    dict_mast = {key: values for key, values in enumerate([x + y for y in ['c', 'd', 'h', 's']
                                                           for x in
                                                           ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q',
                                                            'K']])}
    spis_decode = [dict_mast[i] for i in sorted(cards)]
    return spis_decode


print(encode(["Td", "8c", "Ks"]))
print(encode(["Qh", "5h", "Ad"]))
print(encode(["8c", "Ks", "Td"]))
print(encode(["Qh", "Ad", "5h"]))

print(decode([7, 22, 51]))
print(decode([13, 30, 37]))
print(decode([7, 51, 22]))
print(decode([13, 37, 30]))