def mix(s1, s2):
    list_1 = list({'1:' + i * s1.count(i) if s2.count(i) != s1.count(i) else '=:' + i * s1.count(i) for i in s1 if
                   96 < ord(i) < 123 and s1.count(i) > 1 and s2.count(i) <= s1.count(i)})
    list_2 = list(
        {'2:' + i * s2.count(i) for i in s2 if
         96 < ord(i) < 123 and s2.count(i) > 1 and s2.count(i) != s1.count(i) and s1.count(i) < s2.count(i)})
    list_end = list_2 + list_1
    list_end = sorted(list_end, key=lambda i: (-len(i), i[0], i[2]))

    return '/'.join(list_end)


print(mix("Are they here", "yes, they are here"))
print(mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"))
print(mix("looping is fun but dangerous", "less dangerous than coding"))
print(mix("codewars", "codewars"))
