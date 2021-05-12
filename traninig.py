def nb_year(p0, percent, aug, p):
    sum = 0
    while True:
        p0 = p0+p0*percent/100+aug
        if p > p0:
            sum += 1
        else:
            sum += 1
            break
    return sum

print(nb_year(1500,5,100,5000))