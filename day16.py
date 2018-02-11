import re


def dance(steps):
    programs = list('abcdefghijklmnop')
    possible_states = []
    cycle = 0
    while True:
        for step in steps:
            op, n1, n2 = re.findall(r'(.)(\w+)\/?(\w+)?', step)[0]
            if op == 's':
                n1 = int(n1)
                programs = programs[16 - n1:] + programs[:16 - n1]
            if op == 'x':
                n1 = int(n1)
                n2 = int(n2)
                programs[n1], programs[n2] = programs[n2], programs[n1]
            if op == 'p':
                n1 = programs.index(n1)
                n2 = programs.index(n2)
                programs[n1], programs[n2] = programs[n2], programs[n1]
        prog = ''.join(programs)
        if prog not in possible_states:
            possible_states.append(prog)
        else:
            break
        cycle += 1
    idx = 1000000000 % cycle
    return possible_states[0], possible_states[idx - 1]


with open('data/day16') as f:
    steps = [x for x in f.read().split(',')]
    print(dance(steps))
