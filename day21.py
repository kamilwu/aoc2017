def match(pattern, rule):
    def flip(pattern):  # vertically
        rows = pattern.split('/')
        return '/'.join(list(map(lambda x: x[::-1], rows)))

    def flop(pattern):  # horizontally
        tmp = pattern.split('/')
        tmp.reverse()
        return '/'.join(tmp)

    def transpose(pattern):
        rows = pattern.split('/')
        ret = ''
        for i in range(len(rows)):
            for j in range(len(rows)):
                ret += rows[j][i]
            ret += '/'
        return ret[:len(ret) - 1]

    status = False
    # rotate 90, 180, 270 and 360 (back to normal state)
    for _ in range(4):
        pattern = transpose(pattern)
        pattern = flip(pattern)
        status |= (pattern == rule)
        status |= (rule == flip(pattern))
        status |= (rule == flop(pattern))
    return status


def fragmentize(pattern):
    size = pattern.index('/')
    di = 0
    if size % 2 == 0:
        di = 2  # break pattern into 2x2 squares
    else:
        di = 3  # break pattern into 3x3 squares

    subpatterns = []
    chunks = pattern.split('/')
    for i in range(0, size, di):
        for j in range(0, size, di):
            subpattern = ''
            for k in range(di):
                subpattern += chunks[i + k][j:j + di] + '/'
            subpatterns.append(subpattern[:-1])
    return subpatterns


def merge(subpatterns):
    image = ''
    edge_len = int(len(subpatterns) ** 0.5)

    for i in range(0, len(subpatterns), edge_len):
        chunk_edge_len = subpatterns[i].index('/')
        for j in range(chunk_edge_len):
            for k in range(edge_len):
                image += subpatterns[i + k].split('/')[j]
            image += '/'
    return image[:len(image) - 1]


def iterate(initial, rules_set):
    subpatterns = fragmentize(initial)
    # look-up and apply rules
    for i in range(len(subpatterns)):
        for rule in rules_set:
            if match(subpatterns[i], rule[0]):
                subpatterns[i] = rule[1]
                break
    return merge(subpatterns)


if __name__ == '__main__':
    rules_set = list(map(lambda row: tuple(
        row.rstrip().split(' => ')), open('data/day21').readlines()))
    image = '.#./..#/###'
    for i in range(18):
        image = iterate(image, rules_set)
    # count '#'
    print(image.count('#'))
