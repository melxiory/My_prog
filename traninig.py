def getAllPrimeFactors(n):
    spis = []
    delitel = 2
    if type(n) == str:
        return spis
    if n < 0:
        return spis
    if n == 1:
        spis = [1]
    while n > 1:
        if n % delitel == 0:
            n = n // delitel
            spis.append(delitel)
        else:
            delitel += 1
    return spis


def getUniquePrimeFactorsWithCount(n):
    spis = []
    spis_count = [[], []]
    delitel = 2
    if type(n) == str:
        return spis_count
    if n < 0:
        return spis_count
    if n == 1:
        spis = [1]
    while n > 1:
        if n % delitel == 0:
            n = n // delitel
            spis.append(delitel)
        else:
            delitel += 1
    summator = 0
    spis_count[0].append(spis[0])
    spis_count[1].append(spis.count(spis[0]))
    for i in spis:
        if i != spis_count[0][summator]:
            spis_count[0].append(i)
            spis_count[1].append(spis.count(i))
            summator += 1
    return spis_count


def getUniquePrimeFactorsWithProducts(n):
    spis = []
    spis_count = [[], []]
    spis_products = []
    delitel = 2
    if type(n) == str:
        return spis_products
    if n < 0:
        return spis_products
    if n == 1:
        spis = [1]
    while n > 1:
        if n % delitel == 0:
            n = n // delitel
            spis.append(delitel)
        else:
            delitel += 1
    summator = 0
    spis_count[0].append(spis[0])
    spis_count[1].append(spis.count(spis[0]))
    for i in spis:
        if i != spis_count[0][summator]:
            spis_count[0].append(i)
            spis_count[1].append(spis.count(i))
            summator += 1
    for i, j in zip(spis_count[0], spis_count[1]):
        spis_products.append(i ** j)
    return spis_products


print(getAllPrimeFactors(1))
print(getAllPrimeFactors(100))
print(getAllPrimeFactors(1000))
print(getAllPrimeFactors(1000001))
print()
print(getUniquePrimeFactorsWithCount(1))
print(getUniquePrimeFactorsWithCount(100))
print(getUniquePrimeFactorsWithCount(1000))
print(getUniquePrimeFactorsWithCount(1000001))
print()
print(getUniquePrimeFactorsWithProducts(1))
print(getUniquePrimeFactorsWithProducts(100))
print(getUniquePrimeFactorsWithProducts(1000))
print(getUniquePrimeFactorsWithProducts(1000001))
