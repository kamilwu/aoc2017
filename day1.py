def summation(s):
    res = 0
    for i in range(len(s)):
        if s[i] == s[i - 1]:
            res += int(s[i])
    return res


def summationB(s):
    res = 0
    halfway = int(len(s) / 2)
    for i in range(len(s)):
        if s[i] == s[i - halfway]:
            res += int(s[i])
    return res


if __name__ == "__main__":
    with open("data/day1") as f:
        s = f.read().strip()
        print(summation(s))
        print(summationB(s))
