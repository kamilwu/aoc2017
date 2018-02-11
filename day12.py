def group_by(connections, id):
    group = set()
    stack = [id]
    while stack:
        parent = stack.pop()
        for program in connections[parent]:
            if program not in group:
                group.add(program)
                stack.append(program)
    return group


def num_of_groups(connections):
    group = set()
    unique_groups = 0
    for id in range(len(connections)):
        if id not in group:
            group = group.union(group_by(connections, id))
            unique_groups += 1
    return unique_groups


if __name__ == "__main__":
    connections = []
    with open("data/day12") as f:
        for line in f:
            neighbors = line[line.find('>') + 2:]
            connections.append(set(int(x) for x in neighbors.split(', ')))
    group0 = group_by(connections, 0)
    print("Part 1:", len(group0))
    print("Part 2: ", num_of_groups(connections))
