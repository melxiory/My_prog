import sys, random, bisect

n = int(sys.stdin.readline().strip().split()[0])
left_points, right_points = [0], [0]
for _ in range(n):
    i = tuple(map(int, sys.stdin.readline().strip().split()))
    left_points += [i[0]]
    right_points += [i[1]]
else:
    del left_points[0]
    del right_points[0]
points = list(map(int, sys.stdin.readline().strip().split()))


def partition3(A, l, r):
    lt = l
    i = l
    gt = r
    pivot = A[l]
    while i <= gt:
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > pivot:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1

    return lt, gt


def quick_sort(A, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    A[k], A[l] = A[l], A[k]
    lt, gt = partition3(A, l, r)
    quick_sort(A, l, lt - 1)
    quick_sort(A, gt + 1, r)


def left_segm_p(k):
    acc = 0
    for i in left_points:
        if k >= i:
            acc += len(left_points[left_points.index(i):])
            break
    return acc


def right_segm_p(k):
    acc = 0
    for i in right_points:
        if k > i:
            acc += len(right_points[right_points.index(i):])
            break
    return acc


quick_sort(left_points, 0, len(left_points)-1)
quick_sort(right_points, 0, len(right_points)-1)
for i in range(len(points)):
    points[i] = str(bisect.bisect_right(left_points, points[i]) - bisect.bisect_left(right_points, points[i]))
print(' '.join(points))
