from collections import namedtuple


def severity(layout):
    severity = 0
    for layer in layout:
        offset = layer.depth % ((layer.range - 1) * 2)
        if offset == 0:
            severity += layer.depth * layer.range
    return severity


def breakthrough(layout):
    delay = -1
    ok = False
    while not ok:
        ok = True
        delay += 1
        for layer in layout:
            offset = (layer.depth + delay) % ((layer.range - 1) * 2)
            if offset == 0:
                ok = False
                break
    return delay


if __name__ == "__main__":
    Layer = namedtuple("Layer", "depth range")
    layout = []
    for line in open("data/day13").readlines():
        x, y = line.rstrip().split(": ")
        layer = Layer(int(x), int(y))
        layout.append(layer)

    print("Part1:", severity(layout))
    print("Part2:", breakthrough(layout))
