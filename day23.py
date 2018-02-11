from collections import defaultdict, namedtuple


def execute(instructions):
    registers = defaultdict(int)
    mul_exec, idx = 0, 0
    while idx < len(instructions):
        i = instructions[idx]
        try:
            op2 = int(i.op2)
        except:
            op2 = registers[i.op2]

        if i.mne == "set":
            registers[i.op1] = op2
        elif i.mne == "sub":
            registers[i.op1] -= op2
        elif i.mne == "mul":
            registers[i.op1] *= op2
            mul_exec += 1
        else:  # jnz
            try:
                op1 = int(i.op1)
            except:
                op1 = registers[i.op1]
            if op1 != 0:
                idx += op2 - 1
        idx += 1
    return mul_exec


def optimized_part2(b):
    h = 0
    for d in range(b, b + 17017, 17):
        e = 2
        while e < d / 2:
            if d % e == 0:
                h += 1
                break
            e += 1
    return h


if __name__ == "__main__":
    Instruction = namedtuple("Instruction", "mne op1 op2")
    instructions = []
    for line in open("data/day23").readlines():
        a = line.rstrip().split(' ')
        if len(a) == 2:
            a += ["0"]
        instructions.append(Instruction(a[0], a[1], a[2]))

    part1 = execute(instructions)
    print(part1)

    part2 = optimized_part2(106700)
    print(part2)
