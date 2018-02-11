from collections import namedtuple
from collections import defaultdict


def run(instructions, n):
    programs = [x for x in range(n)]
    register_set, que = [], []
    for i in range(n):
        register_set.append(defaultdict(int))
    register_set[1]['p'] = 1
    que = [[] for _ in range(n)]
    pc = [0] * n
    sc = [0] * n  # Send counter
    wait = [False] * n
    terminate = [False] * n

    while True:
        pcs = pc[:]
        for pid in programs:
            if terminate[pid]:
                continue
            i = instructions[pc[pid]]
            registers = register_set[pid]
            op2 = 0
            try:
                op2 = int(i.op2)
            except:
                op2 = registers[i.op2]

            if wait[pid] and len(que[pid]) == 0:
                continue
            else:
                wait[pid] = False
            if i.mne == "set":
                registers[i.op1] = op2
            elif i.mne == "snd":
                que[pid ^ 1].insert(0, registers[i.op1])
                sc[pid] += 1
            elif i.mne == "add":
                registers[i.op1] += op2
            elif i.mne == "mul":
                registers[i.op1] *= op2
            elif i.mne == "mod":
                registers[i.op1] %= op2
            elif i.mne == "rcv":
                if len(que[pid]) != 0:
                    registers[i.op1] = que[pid].pop()
                else:
                    wait[pid] = True
                    continue
            elif i.mne == "jgz":
                op1 = 0
                try:
                    op1 = int(i.op1)
                except:
                    op1 = registers[i.op1]
                if op1 > 0:
                    pc[pid] += op2 - 1
            pc[pid] += 1
            if pc[pid] >= len(instructions):  # No further instructions
                terminate[pid] = True
        if pcs == pc:  # Program counters didn't changed, deadlock detected
            break
        if terminate[0] and terminate[1]:
            break
    print(sc[1])


def execute(instructions):
    registers = defaultdict(int)
    last_played, idx = 0, 0

    while idx <= len(instructions):
        i = instructions[idx]
        op2 = 0
        try:
            op2 = int(i.op2)
        except:
            op2 = registers[i.op2]

        if i.mne == "set":
            registers[i.op1] = op2
        elif i.mne == "snd":
            last_played = registers[i.op1]
        elif i.mne == "add":
            registers[i.op1] += op2
        elif i.mne == "mul":
            registers[i.op1] *= op2
        elif i.mne == "mod":
            registers[i.op1] %= op2
        elif i.mne == "rcv" and registers[i.op1] != 0:
            print(last_played)
            return
        elif i.mne == "jgz":
            op1 = 0
            try:
                op1 = int(i.op1)
            except:
                op1 = registers[i.op1]
            if op1 > 0:
                idx += op2 - 1
        idx += 1


Instruction = namedtuple("Instruction", "mne op1 op2")
instructions = []
for line in open("data/day18").readlines():
    a = line.rstrip().split(' ')
    if len(a) == 2:
        a += ["0"]
    instructions.append(Instruction(a[0], a[1], a[2]))
execute(instructions)
run(instructions, 2)
