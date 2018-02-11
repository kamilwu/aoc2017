from collections import defaultdict

if __name__ == "__main__":
    with open("data/day8") as f:
        registers = defaultdict(int)
        max_ever = float('-inf')
        for line in f:
            reg, op, val, _, cond_reg, cond_op, cond_val = line.split(' ')

            value = int(val) if op == "inc" else -1 * int(val)
            condition = "registers['{}'] {} {}".format(
                cond_reg, cond_op, cond_val)
            if eval(condition):
                registers[reg] += value
                if registers[reg] > max_ever:
                    max_ever = registers[reg]
        print("max:", max(list(registers.values())))
        print("max_ever:", max_ever)
