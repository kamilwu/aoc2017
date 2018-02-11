import re
import collections


def get_root():
    def weight_summation(program):
        subprograms = children[program]
        subprograms_weight = [weight_summation(
            subprogram) for subprogram in subprograms]
        if len(set(subprograms_weight)) > 1:
            (target, _), (failure, _) = collections.Counter(
                subprograms_weight).most_common(2)
            failure_program = subprograms[subprograms_weight.index(failure)]
            failure_weight = weights[failure_program]
            print("Proper weight:", failure_weight - (failure - target))
        return sum(subprograms_weight) + weights[program]

    with open("data/day7") as f:
        weights, children = {}, {}
        for line in f:
            line = line.rstrip()
            label, n, *ch = re.findall(r'\w+', line)
            weights[label] = int(n)
            children[label] = ch

        # Get root program name
        root, = set(children) - {x for xs in children.values() for x in xs}
        # Get root's children weights
        weight_summation(root)
        # print(total_weight(root))
        return root


if __name__ == "__main__":
    print(get_root())
