def turn(direction, right):
    if (right and direction[0] == 0) or (not right and direction[1] == 0):
        direction = tuple(x * -1 for x in direction)
    return direction


def simulate(grid, bursts):
    direction = -1, 0
    x = len(grid) // 2
    y = x
    infections = 0

    disease_set = set()
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '#':
                disease_set.add((i, j))

    for _ in range(bursts):
        direction = direction[::-1]
        if (x, y) in disease_set:
            # turn right
            direction = turn(direction, True)
            disease_set.remove((x, y))
        else:
            # turn left
            direction = turn(direction, False)
            disease_set.add((x, y))
            infections += 1

        # move forward
        x += direction[0]
        y += direction[1]

    return infections


def simulate_evolved(grid, bursts):
    direction = -1, 0
    x = len(grid) // 2
    y = x
    infections = 0

    disease_map = {}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '#':
                disease_map[(i, j)] = 'i'

    for _ in range(bursts):
        if (x, y) in disease_map:
            status = disease_map[(x, y)]

            if status == 'w':  # infect
                infections += 1
                disease_map[(x, y)] = 'i'
            elif status == 'i':  # turns right, set as flagged
                direction = direction[::-1]
                direction = turn(direction, True)
                disease_map[(x, y)] = 'f'
            else:  # reverse direction, make clean
                direction = tuple(x * -1 for x in direction)
                disease_map.pop((x, y))
        else:  # turns left, make weak
            direction = direction[::-1]
            direction = turn(direction, False)
            disease_map[(x, y)] = 'w'

        # move forward
        x += direction[0]
        y += direction[1]

    return infections


if __name__ == '__main__':
    grid = [x.rstrip() for x in open('data/day22').readlines()]
    no = simulate(grid, 10000)
    print(no)

    no = simulate_evolved(grid, 10000000)
    print(no)
