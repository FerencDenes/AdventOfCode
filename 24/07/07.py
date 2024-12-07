input = [line for line in open('input.txt').read().split('\n') ]

def opPipe(a,b):
    return int(str(a)+str(b))

def findOperators(sum, pos, prefSum, list):
    if prefSum == sum and pos == len(list):
        return True
    if prefSum > sum or pos >= len(list):
        return False
    return findOperators(sum, pos + 1, prefSum + list[pos], list) or findOperators(sum, pos + 1, prefSum * list[pos], list)

def findOperators2(sum, pos, prefSum, list):
    if prefSum == sum and pos == len(list):
        return True
    if prefSum > sum or pos >= len(list):
        return False
    return findOperators2(sum, pos + 1, prefSum + list[pos], list) or findOperators2(sum, pos + 1, prefSum * list[pos], list) or findOperators2(sum, pos + 1, opPipe(prefSum, list[pos]), list)

res1 = 0
res2 = 0
for line in input:
    sp = line.split(': ')
    list = [int(x) for x in sp[1].split()]
    if findOperators(int(sp[0]), 1, list[0], list):
        res1 += int(sp[0])
        res2 += int(sp[0])
    elif findOperators2(int(sp[0]), 1, list[0], list):
        res2 += int(sp[0])
print(res1)
print(res2)