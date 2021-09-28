def moving_shift(s, shift):
    alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    strok_shift = ''
    for i in s:
        if i.isupper():
            strok_shift += alfavit[(alfavit.find(i) + shift) % len(alfavit)]
            shift += 1
        elif not i.isalpha() or i in 'éâè':
            strok_shift += i
            shift += 1
        else:
            strok_shift += alfavit[(alfavit.find(i.upper()) + shift) % len(alfavit)].lower()
            shift += 1
    split_strok_cel = (len(strok_shift) - 1) // 5
    list_itog = []
    for j in range(4):
        list_itog.append(strok_shift[:split_strok_cel + 1])
        strok_shift = strok_shift[split_strok_cel + 1:]
    else:
        list_itog.append(strok_shift)
    return list_itog


def demoving_shift(s, shift):
    alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = ''.join(s)
    strok_shift = ''
    for i in s:
        if i.isupper():
            strok_shift += alfavit[(alfavit.find(i) - shift) % len(alfavit)]
            shift += 1
        elif not i.isalpha() or i in 'éâè':
            strok_shift += i
            shift += 1
        else:
            strok_shift += alfavit[(alfavit.find(i.upper()) - shift) % len(alfavit)].lower()
            shift += 1
    return strok_shift


print(moving_shift('os  afneewuftllzisohtj tbeca gikgeeeuiJ azxsoxaiOstaeaoemy eioecusdaorod eLiaaka', 13))
print(
    demoving_shift(moving_shift('os  afneewuftllzisohtj tbeca gikgeeeuiJ azxsoxaiOstaeaoemy eioecusdaorod eLiaaka', 13),
                   13))
