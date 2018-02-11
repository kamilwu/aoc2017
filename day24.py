def build(components, last=0):
    highscore, longest = 0, 0
    high, long = [], []

    for c in components:
        if c[0] == last or c[1] == last:
            components_ = components[:]
            components_.remove(c)
            tail = build(components_, c[1] if c[0] == last else c[0])

            x = c + tail[0]
            if sum(x) > highscore:
                highscore = sum(x)
                high = x

            x = c + tail[1]
            if len(x) > longest:
                longest = len(x)
                long = x

    return high, long


if __name__ == '__main__':
    input = [list(map(int, x.rstrip().split('/')))
             for x in open('data/day24').readlines()]
    x = build(input)

    print(sum(x[0]))
    print(sum(x[1]))
