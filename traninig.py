def zero(arg=None):
    if not arg:
        return 0
    else:
        return eval(f'0{arg}')


def one(arg=None):
    if not arg:
        return 1
    else:
        return eval(f'1{arg}')


def two(arg=None):
    if not arg:
        return 2
    else:
        return eval(f'2{arg}')


def three(arg=None):
    if not arg:
        return 3
    else:
        return eval(f'3{arg}')


def four(arg=None):
    if not arg:
        return 4
    else:
        return eval(f'4{arg}')


def five(arg=None):
    if not arg:
        return 5
    else:
        return eval(f'5{arg}')


def six(arg=None):
    if not arg:
        return 6
    else:
        return eval(f'6{arg}')


def seven(arg=None):
    if not arg:
        return 7
    else:
        return eval(f'7{arg}')


def eight(arg=None):
    if not arg:
        return 8
    else:
        return eval(f'8{arg}')


def nine(arg=None):
    if not arg:
        return 9
    else:
        return eval(f'9{arg}')


def plus(arg):
    return f'+{arg}'


def minus(arg):
    return f'-{arg}'


def times(arg):
    return f'*{arg}'


def divided_by(arg):
    return f'//{arg}'


print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))
