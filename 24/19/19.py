import re

input = [line.strip() for line in open("input.txt").readlines()]

towels = input[0].split(", ")
regexString = "|".join(towels)
towelRegexp = rf"^({regexString})+$"
res1 = 0
for line in input[2:]:
    if re.match(towelRegexp, line):
        res1 += 1
print(res1)

memo = dict()
memo[""] = 1
def matchTowel(line):
    if line in memo:
        return memo[line]
    ret = 0
    for towel in towels:
        if line.startswith(towel):
            ret += matchTowel(line[len(towel):])
    memo[line] = ret
    return ret

res2 = 0
for line in input[2:]:
    res2 += matchTowel(line)
print(res2)