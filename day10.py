def calc_sparse_hash(lengths, size, runs):
    idx, skip = 0, 0
    data = [x for x in range(size)]
    for _ in range(runs):
        for length in lengths:
            ddata = data * 2
            underflow = length + idx - size
            if underflow < 0:
                underflow = 0
            ddata[idx:idx + length] = reversed(ddata[idx:idx + length])
            data = ddata[size:size + underflow] + ddata[underflow:size]
            idx += length + skip
            idx = idx % size
            skip += 1
    return data


def to_dense_hash(sparse_hash):
    def chunks(l, n):
        for i in range(0, len(l), n):
            xor = 0
            for item in l[i:i + n]:
                xor ^= item
            yield xor
    return list(chunks(sparse_hash, 16))


def to_hex(dense_hash):
    hash = ""
    for item in dense_hash:
        hash += hex(item)[2:].zfill(2)
    return hash


def knothash(lengths):
    lengths += [17, 31, 73, 47, 23]
    sparse = calc_sparse_hash(lengths, 256, 64)
    return to_hex(to_dense_hash(sparse))


if __name__ == "__main__":
    input = open("data/day10").read()
    # part 1)
    lengths = [int(x) for x in input.split(',')]
    ret = calc_sparse_hash(lengths, 256, 1)

    # part 2)
    lengths = [int(x) + 48 if x != ',' else 44 for x in input]
    ret2 = knothash(lengths)

    print("Part 1: ", ret[0] * ret[1])
    print("Part 2: ", ret2)
