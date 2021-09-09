def my_crib(n):
    home_roof = f'{"  " * n}{"_" * ((n - 1) * 2 + 3)}{"  " * n}\n'
    home_side = ''
    for roof_side in range(n * 2 - 1):
        home_roof += f'{" " * (n * 2 - roof_side - 1)}/{"_" * ((n - 1) * 2 + 3) + "__" * roof_side}\\{" " * (n * 2 - roof_side - 1)}\n'
        if n * 2 - (roof_side+1) > n:
            home_side += f'|{"     " + " " * ((n - 1) * 6)}|\n'
        elif n * 2 - (roof_side+1) == n:
            home_side += f'|{" " * (n*2-1)} {"_" * (n*2-1)} {" " * (n*2-1)}|\n'
        else:
            home_side += f'|{" " * (n*2-1)}|{" " * (n*2-1)}|{" " * (n*2-1)}|\n'
    else:
        home_roof += f'/{"_____" + "_" * ((n - 1) * 6)}\\\n'
        home_side += f'|{"_" * (n*2-1)}|{"_" * (n*2-1)}|{"_" * (n*2-1)}|'
    return home_roof + home_side


print(my_crib(1))
print(my_crib(2))
print(my_crib(3))
