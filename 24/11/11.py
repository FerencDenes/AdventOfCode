from collections import defaultdict

input = [int(line) for line in open('input.txt').read().split()]
inp = input.copy()
def transform(nums):
    nextRound = []
    for i in range(len(nums)):
        num = nums[i]
        strNum = str(num)
        if num == 0:
            nextRound.append(1)
        elif len(strNum) % 2 == 0:
            nextRound.append(int(strNum[0:len(strNum)//2]))
            nextRound.append(int(strNum[len(strNum)//2:]))
        else:
            nextRound.append(num*2024)
    return nextRound

for blink in range(25):
    inp = transform(inp)
print(len(inp))

def transform2(numMap):
    res = defaultdict(int)
    for k, v in numMap.items():
        strNum = str(k)
        if k == 0:
            res[1] += v
        elif len(strNum) % 2 == 0:
            res[int(strNum[0:len(strNum)//2])] += v
            res[int(strNum[len(strNum)//2:])] += v
        else:
            res[k*2024] += v
    return res

numMap = defaultdict(int)
for num in input:
    numMap[num] += 1
for blink in range(75):
    numMap = transform2(numMap)

print(sum(numMap.values()))