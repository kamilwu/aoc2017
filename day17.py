times = 301


def generator(iterable, i=0):
    while True:
        while i < len(iterable):
            yield (iterable[i], i)
            i += 1
        i = 0


def spinlock(times):
    sp = [0]
    idx = 0
    for i in range(1, 2018):
        gen = generator(sp, idx)
        idx = -1
        for _ in range(times + 1):
            _, idx = next(gen)
        sp.insert(idx + 1, i)
        if idx == 0:
            print(i)
        idx = idx + 1
    return sp


def spinlock_i(times):
    idx, len = 0, 1
    for i in range(1, 40000000):
        idx += times
        idx = idx % len
        if idx == 0:
            print(i)
        len += 1
        idx += 1


sp = spinlock(times)
print("Part1: ", sp[sp.index(2017) + 1])
print("Part2: ")
spinlock_i(times)
