import math


def next_larger_than(value):
    size = 19
    grid = [[0] * size for i in range(size)]

    medium = int(size / 2)
    edge_len = 1
    i, j = medium, medium
    grid[i][j] = 1
    while True:
        for step in range(edge_len):  # right
            j += 1
            current = assign(grid, i, j)
            if current > value:
                return current
        for step in range(edge_len):  # top
            i -= 1
            current = assign(grid, i, j)
            if current > value:
                return current
        edge_len += 1
        for step in range(edge_len):  # left
            j -= 1
            current = assign(grid, i, j)
            if current > value:
                return current
        for step in range(edge_len):  # bottom
            i += 1
            current = assign(grid, i, j)
            if current > value:
                return current
        edge_len += 1


def assign(grid, i, j):
    sum = 0
    sum += grid[i - 1][j - 1]
    sum += grid[i - 1][j]
    sum += grid[i - 1][j + 1]
    sum += grid[i][j - 1]
    sum += grid[i][j + 1]
    sum += grid[i + 1][j - 1]
    sum += grid[i + 1][j]
    sum += grid[i + 1][j + 1]
    grid[i][j] = sum
    return sum


def steps(index):
    s = math.sqrt(index)
    # Get spiral no. (x cord)
    i = 1
    while s > i:
        i += 2
    spiral = int(i / 2)
    # Get y cord
    biggest = 1
    for k in range(spiral):
        biggest += 8 * (k + 1)
    y = _iter(spiral, index, biggest)
    return y + spiral


def _iter(maximum, start, end):
    i = end - start
    ret = maximum
    dec = True
    for _ in range(i):
        if dec:
            ret -= 1
        else:
            ret += 1
        if ret == maximum or ret == 0:
            dec = not dec
    return ret


if __name__ == "__main__":
    print(steps(265149))
    print(next_larger_than(265149))
