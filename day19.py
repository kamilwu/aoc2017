def route(route_table):
    x = route_table[0].index('|')
    y = 0
    step = 1
    trail = ''
    vertically = True
    length = len(route_table[0])
    num_steps = 0

    while True:
        while route_table[y][x] != '+':
            if route_table[y][x] not in '-|':
                trail += route_table[y][x]
            if route_table[y][x] == ' ':
                return trail, num_steps
            if vertically:
                y += step
            else:
                x += step
            num_steps += 1

        vertically = not vertically
        if vertically:
            if y - 1 >= 0 and y - 1 < length and route_table[y - 1][x] == '|':
                step = -1
                y -= 1
            else:
                step = 1
                y += 1
        else:
            if x + 1 >= 0 and x + 1 < length and route_table[y][x + 1] == '-':
                step = 1
                x += 1
            else:
                step = -1
                x -= 1
        num_steps += 1


with open('data/day19') as f:
    route_table = [x[:len(x) - 1] for x in f.readlines()]
    print(route(route_table))
