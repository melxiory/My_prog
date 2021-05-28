def find_even_index(arr):
    for i in range(len(arr)):
        a = sum(arr[0:i])
        b = sum(arr[i+1:len(arr)])
        if a == b:
            return i
    return -1

print(find_even_index([10,-80,10,10,15,35,20]))