def likes(names):
    if names == []:
        return 'no one likes this'
    if len(names) == 1:
        return f'{names[0]} likes this'
    if len(names) == 2:
        return f'{names[0]} and {names[1]} likes this'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} likes this'
    if len(names) > 3:
        return f'{names[0]}, {names[1]} and {len(names)-2} others likes this'


print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))