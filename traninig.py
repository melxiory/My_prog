def Xbonacci(signature, n):
    if len(signature)< n:
        sum_1 = 0
        spis = signature[:]
        for i in range(len(signature), n):
            for j in range(1, len(signature)+1):
                sum_1 += spis[i-j]
            spis.append(sum_1)
            sum_1 = 0
    else:
        if n:
            spis = signature[:n]
        else:
            spis = []
    return spis

print(Xbonacci([0,1],10))
print(Xbonacci([1,1],10))
print(Xbonacci([0,0,0,0,1],10))
print(Xbonacci([1,0,0,0,0,0,1],10))
print(Xbonacci([1,0,0,0,0,0,0,0,0,0],20))