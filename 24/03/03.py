import re
input = [line for line in open('input.txt').read().split('\n') ]
mulPattern = r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))"
numPattern = r"\d+"
res1 = 0
res2 = 0
doMul = True
for line in input:
    muls = re.findall(mulPattern, line)
    for mul in muls:
        if mul[0]:
            nums = [int(x) for x in re.findall(numPattern, mul[0])]
            res1 += nums[0] * nums[1]
            if doMul:
                res2 += nums[0] * nums[1]
        if mul[1]:
            doMul = True
        if mul[2]:
            doMul = False
print(res1)
print(res2)
