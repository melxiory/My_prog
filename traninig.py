def comp(array1, array2):
    if array1 == None and array2 == [] or array2 == None and array1 == [] or len(array1) != len(array2):
        return False
    if  array1 == array2 ==[]:
        return True
    array1.sort()
    array2.sort()
    if array1[0] < 0:
        array1 = [abs(i) for i in array1]
        array1.sort()
    if array2[0] < 0:
        array2 = [abs(i) for i in array2]
        array2.sort()
    for i in range(len(array1)):
        if array1[i] ** 2 != array2[i]:
            return False
    return True

print(comp([-121, -144, 19, -161, 19, -144, 19, -11], [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]))
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]))
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]))