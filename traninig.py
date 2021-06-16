def Xbonacci(signature, n):
    output, x = signature[:n], len(signature)
    while len(output) < n:
        output.append(sum(output[-x:]))
    return output

print(Xbonacci([0,1],10))
print(Xbonacci([1,1],10))
print(Xbonacci([0,0,0,0,1],10))
print(Xbonacci([1,0,0,0,0,0,1],10))
print(Xbonacci([1,0,0,0,0,0,0,0,0,0],20))