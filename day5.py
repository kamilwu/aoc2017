def steps(instructions, stranger_mode):
    i, steps = 0, 0
    while i < len(instructions) and i >= 0:
        jump_by = instructions[i]
        if instructions[i] >= 3 and stranger_mode:
            instructions[i] -= 1
        else:
            instructions[i] += 1
        i += jump_by
        steps += 1
    return steps


if __name__ == "__main__":
    print(steps([0, 3, 0, 1, -3], True))
    with open("data/day5") as f:
        instructions = [int(x.rstrip()) for x in f]
        print(steps(instructions[:], False))
        print(steps(instructions[:], True))
