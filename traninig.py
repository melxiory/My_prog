def land_perimeter(arr):
    def numofneighbour(mat, i, j):
        count = 0
        # UP
        if (i > 0 and mat[i - 1][j]):
            count += 1
        # LEFT
        if (j > 0 and mat[i][j - 1]):
            count += 1
        # DOWN
        if (i < R - 1 and mat[i + 1][j]):
            count += 1
        # RIGHT
        if (j < C - 1 and mat[i][j + 1]):
            count += 1
        return count
    arr = [list(i) for i in arr]
    R = len(arr)
    C = len(arr[0])
    spis = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "X":
                arr[i][j] = 1
            else:
                arr[i][j] = 0
    perimeter = 0
    for i in range(0, R):
        for j in range(0, C):
            if arr[i][j]:
                perimeter += (4 - numofneighbour(arr, i, j))
    return f"Total land perimeter: {perimeter}"




print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]))
print(land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]))
print(land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]))
print(land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]))
print(land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]))