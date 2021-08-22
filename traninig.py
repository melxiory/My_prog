import re


def regular_expressions(n):
    valid_date = re.search(r'\[((02-((1\d|0[1-9])|2[0-8]))|((1[0-2]|0([1]|[3-9]))-(([1-2]\d|0[1-9])|3[0-1])))]', n)
    return valid_date.group(0)

print(regular_expressions("[[[08-29]]]"))
print(regular_expressions("[01-23]"))
print(regular_expressions("[02-16]"))
print(regular_expressions("[02-31]"))
print(regular_expressions("[ 6-03]"))
print(regular_expressions("ignored [08-11] ignored"))
print(regular_expressions("[3] [12-04] [09-tenth]"))
print(regular_expressions("[02-00]"))
print(regular_expressions("[02-[08-11]04]"))
