import csv

with open('Crimes.csv') as crim:
    reader = csv.reader(crim)
    read_it = iter(reader)
    ind = next(read_it).index('Primary Type')
    dict_cr = {}
    for i in read_it:
        if i[ind] not in dict_cr:
            dict_cr[i[ind]] = 1
        else:
            dict_cr[i[ind]] += 1
    max = ''
    for i in dict_cr:
        if not max:
            max = i
        if dict_cr[max] < dict_cr[i]:
            max = i
    print(max)
