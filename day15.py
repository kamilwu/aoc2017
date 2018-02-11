gen_a_seed = 116
gen_b_seed = 299


def generator(seed, factor, criteria):
    while True:
        val = seed * factor
        seed = val % 2147483647
        if seed % criteria == 0:
            yield seed


def judge(times):
    gen_a = generator(gen_a_seed, 16807, 4)
    gen_b = generator(gen_b_seed, 48271, 8)

    matches = 0
    for _ in range(times):
        a = next(gen_a)
        b = next(gen_b)
        if (a & 0xFFFF) == (b & 0xFFFF):
            matches += 1

    return matches


# part1 = judge(40000000)
part2 = judge(5000000)
# print(part1)
print(part2)
