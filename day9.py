def score(data):
    score, score_level, trash = 0, 0, 0
    is_garbage, skip = False, False
    for ch in data:
        if skip:
            skip = False
            continue
        elif ch == '!':
            skip = True
        elif ch == '>':
            is_garbage = False
        elif is_garbage:
            trash += 1
            continue
        elif ch == '{':
            score_level += 1
        elif ch == '}':
            score += score_level
            score_level -= 1
        elif ch == '<':
            is_garbage = True
    return score, trash


if __name__ == "__main__":
    print(score(open("data/day9").read()))
