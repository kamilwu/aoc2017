from numpy import array


def traverse(steps):
    pos = array([0, 0, 0])

    def distance(x): return (abs(x[0]) + abs(x[1]) + abs(x[2])) / 2
    max = 0

    for step in steps:
        if step == 'nw':
            pos += array([-1, 1, 0])
        elif step == 'n':
            pos += array([0, 1, -1])
        elif step == 'ne':
            pos += array([1, 0, -1])
        elif step == 'se':
            pos += array([1, -1, 0])
        elif step == 's':
            pos += array([0, -1, 1])
        else:
            pos += array([-1, 0, 1])
        max = distance(pos) if distance(pos) > max else max

    return distance(pos), max


if __name__ == '__main__':
    steps = [x for x in open('data/day11').read().rstrip().split(',')]
    num = traverse(steps)

    print(num)
