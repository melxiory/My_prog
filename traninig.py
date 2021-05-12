def duplicate_count(text):
    if text.isalnum():
        text = text.lower()
        sum = 0
        k = 0
        while True:
            if text.count(text[sum]) >= 2:
                otsec = text[sum]
                for i in text:
                    if otsec == i:
                        text = text[0:text.index(i)] + text[text.index(i)+1:len(text)]
                k += 1
            else:
                sum += 1
            if sum == len(text):
                return k
    else:
        return 0



slov=input('Введите слово - ')

print(duplicate_count(slov))
