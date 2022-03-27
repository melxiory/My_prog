from collections import Counter
comb = input().split()
mean = {
         '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
         '10':10,'J':11,'Q':12,'K':13,'A':14
         }
lear = Counter([i[-1] for i in comb])
val = Counter([mean[i[0:-1]] for i in comb])
if len(lear) == 1:
    if set(val.keys()) == {10, 11, 12, 13, 14}:
        print('Royal Flush')
    elif set(val.keys()) == set(range(min(val.keys()), min(val.keys()) + 5)):
        print('Straight Flush')
    else:
        print('Flush')
elif 4 in val.values():
    print('Four of a Kind')
elif {2, 3} == set(val.values()):
    print('Full House')
elif set(val.keys()) == set(range(min(val.keys()), min(val.keys()) + 5)):
    print('Straight')
elif 3 in val.values():
    print('Three of a Kind')
elif list(val.values()).count(2) == 2:
    print('Two Pairs')
elif 2 in val.values():
    print('Pair')
else:
    print('High Card')