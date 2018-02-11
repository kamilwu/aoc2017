def realloc_cycles(memory_banks):
    banks = memory_banks
    cycles = 0
    history = [banks[:]]
    size = len(banks)
    # While there are no duplicates of the last element
    while history[-1] not in history[:len(history) - 1]:
        biggest = max(banks)
        index = banks.index(biggest)
        blocks_to_redistribute = biggest if (biggest < size) else size
        banks[index] -= blocks_to_redistribute
        for i in range(blocks_to_redistribute):
            banks[(index + 1 + i) % size] += 1
        history.append(banks[:])
        cycles += 1
    # Get the size of the loop
    idx = history.index(history[-1])
    loop_size = cycles - idx
    return cycles, loop_size


if __name__ == "__main__":
    with open("data/day6") as f:
        banks = [int(x) for x in f.readline().split('\t')]
        print(realloc_cycles(banks))
