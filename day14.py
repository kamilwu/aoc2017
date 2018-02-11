from data/day10 import knothash


def get_disk_grid(puzzle):
    grid = []
    for i in range(128):
        input = [ord(x) for x in "{}-{}".format(puzzle, i)]
        khash = knothash(input)
        grid.append(format(int(khash, 16), 'b').zfill(128))
    return grid


def get_regions(grid):
    def wipe(x, y):
        seen.add((x, y))
        cords = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
        for xc, yc in cords:
            if xc < 0 or yc < 0 or xc >= 128 or yc >= 128:
                continue
            if grid[xc][yc] == '1' and (xc, yc) not in seen:
                wipe(xc, yc)

    seen = set()
    n = 0
    for x in range(128):
        for y in range(128):
            if grid[x][y] == '1' and (x, y) not in seen:
                wipe(x, y)
                n += 1
    for row in grid:
        print(row)
    return n


if __name__ == "__main__":
    puzzle = "ugkiagan"
    grid = get_disk_grid(puzzle)
    usage = sum([row.count('1') for row in grid])
    print("Part1:", usage)
    print("Part2:", get_regions(grid))
