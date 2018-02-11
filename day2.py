import re


def evenly_divisible(nums):
    for i, num in enumerate(nums):
        for j in range(len(nums)):
            if i != j and num % nums[j] == 0:
                return num / nums[j]


def proceed():
    with open("data/day2") as f:
        sum1, sum2 = 0, 0
        for line in f:
            nums = [int(x) for x in re.findall(r'\d+', line)]
            sum1 += max(nums) - min(nums)
            sum2 += evenly_divisible(nums)
        return sum1, sum2


if __name__ == "__main__":
    print(proceed())
