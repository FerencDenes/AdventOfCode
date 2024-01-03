import re
from collections import defaultdict
# 5,0,238~8,0,238
pattern = re.compile(r'(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)')
input = [ tuple(int(i) for i in re.search(pattern,line).groups()) for line in open('22/input.txt').read().split('\n') ]

input.sort(key=lambda x: min(x[2],x[5]))

positions = {}

def free(brick, shift):
    for x in range(brick[0], brick[3] + 1):
        for y in range(brick[1], brick[4] + 1):
            for z in range(brick[2], brick[5] + 1):
                if (x, y, z - shift) in positions:
                    return False
    return True

for i in range(len(input)):
    brick = input[i]
    bottom = min(brick[2],brick[5])
    sh = 0
    while bottom > 1 and free(brick, sh+1):
        sh += 1
        bottom -= 1
    brick = (brick[0], brick[1], brick[2] - sh, brick[3], brick[4], brick[5] - sh)
    input[i] = brick
    for x in range(brick[0], brick[3] + 1):
        for y in range(brick[1], brick[4] + 1):
            for z in range(brick[2], brick[5] + 1):
                positions[(x, y, z)] = i

def otherSupports(brick, current):
    currentId = positions[current[0], current[1], current[2]]
    brickId = positions[brick[0], brick[1], brick[2]]
    for x in range(brick[0], brick[3] + 1):
        for y in range(brick[1], brick[4] + 1):
            for z in range(brick[2], brick[5] + 1):
                supporter = positions.get((x,y,z-1))
                if supporter != None and supporter != currentId and supporter != brickId:
                    return True
    return False
                    
                
def safeToDisintegrate(brick):
    for x in range(brick[0], brick[3] + 1):
        for y in range(brick[1], brick[4] + 1):
            for z in range(brick[2], brick[5] + 1):
                supported = positions.get((x,y,z+1))
                if supported != None and supported != positions[(x,y,z)]:
                    sb = input[supported]
                    if not otherSupports(sb, brick):
                        return False
    return True

sum =0
for brick in input:
    if safeToDisintegrate(brick):
        sum += 1

print(sum)

supportGraph = defaultdict(set)
supporterGraph = defaultdict(set)
for brick in input:
    for x in range(brick[0], brick[3] + 1):
        for y in range(brick[1], brick[4] + 1):
            for z in range(brick[2], brick[5] + 1):
                supporter = positions.get((x,y,z-1))
                if supporter != None and supporter != positions[(x,y,z)]:
                    supportGraph[supporter].add(positions[(x,y,z)])
                    supporterGraph[positions[(x,y,z)]].add(supporter)

def disintegrate(brickId, toppled):
    nowToppled = []
    if not brickId in supportGraph:
        return 0
    for supported in supportGraph[brickId]:

        willTopple = True
        for s2 in supporterGraph[supported]:
            if s2 != brickId and s2 not in toppled:
                willTopple = False
                break
        if willTopple:
            nowToppled.append(supported)
            toppled.add(supported)
    dsum =0
    for t in nowToppled:
        dsum+=disintegrate(t, toppled)
    return len(toppled)

sum2=0
for brickId in supportGraph:
    s = disintegrate(brickId, set())
    sum2 += s
print(sum2)
    
        
