import sys


def spiral_gen(start_cell, max_cell, walk_order):
    def move(pos, dif):
        return (pos[0] + dif[0], pos[1] + dif[1])

    pos = (start_cell, start_cell)

    cells_total = max_cell ** 2
    cells_curr = 0
    direction = 0

    cols_visited = [start_cell, ]
    rows_visited = [start_cell, ]

    while cells_curr < cells_total:
        cells_curr += 1
        yield pos
        pos = move(pos, walk_order[direction])
        if (pos[0] not in rows_visited) or (pos[1] not in cols_visited):
            if pos[0] not in rows_visited:
                rows_visited.append(pos[0])
            elif pos[1] not in cols_visited:
                cols_visited.append(pos[1])

            direction += 1
            if direction == len(walk_order):
                direction = 0


def print_matrix(matrix: object, item_format: object = '{:03}') -> object:
    print('\n'.join([' '.join(map(lambda a: item_format.format(a), row)) for row in matrix]))


def main(args):
    n = int(input())
    n_max = 2 * n + 1

    A = [[0 for col in range(n_max)] for row in range(n_max)]
    val = 0

    ccw = (
        (-1, 0),
        (0, -1),
        (1, 0),
        (0, 1)
    )

    for row, col in spiral_gen(n, n_max, ccw):
        A[row][col] = val
        val += 1
    print_matrix(A, '{:03}')
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))