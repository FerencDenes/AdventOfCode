from datetime import datetime
input = [ list(line) for line in open('14/input.txt').read().split('\n') ]

rocks = set()
blocks = set()
l = len(input)
w = len(input[0])
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == 'O':
            rocks.add((i,j))
        elif input[i][j] == '#':
            blocks.add((i,j))

def findLoad(input):
        sum = 0
        for j in range(len(input[0])):
            pos = len(input)
            for i in range(len(input)):
                if input[i][j] == 'O':
                    sum += pos
                    pos-=1
                elif input[i][j] == '#':
                    pos = len(input) - i - 1
        return sum

print(findLoad(input))   

memo = {}
def cycle(rocks):
    t = tuple(rocks)
    if t in memo:
        return memo[t]
    retn = set()
    # North
    for j in range(w):

        pos = 0
        for i in range(l):
            if (i,j) in rocks:
                retn.add((pos,j))
                pos+=1
            elif (i,j) in blocks:
                pos = i+1
    # West
    retw= set()
    for i in range(l):
        pos = 0
        for j in range(w):
            if (i,j) in retn:
                retw.add((i,pos))
                pos+=1
            elif (i,j) in blocks:
                pos = j+1
    # South
    rets = set()
    for j in range(w):
        pos = l-1
        for i in range(l-1, -1, -1):
            if (i,j) in retw:
                rets.add((pos,j))
                pos-=1
            elif (i,j) in blocks:
                pos = i-1
    # East
    rete = set()
    for i in range(l):
        pos = w-1
        for j in range(w-1, -1, -1):
            if (i,j) in rets:
                rete.add((i,pos))
                pos-=1
            elif (i,j) in blocks:
                pos = j-1
    memo[tuple(rocks)] = rete
    return rete



start = datetime.now().timestamp()
memolength = -1

cy = 0
# Warmup
while len(memo) != memolength:
    cy += 1
    memolength = len(memo)
    rocks = cycle(rocks)

#Cycle length
cl = 0
rocksAfterCycle = rocks
while rocks != rocksAfterCycle or cl == 0:
    cl += 1
    rocksAfterCycle = cycle(rocksAfterCycle)

cs = (1000000000 - cy) % cl
for i in range(cs):
    rocks = cycle(rocks)

def load(rocks):
    sum = 0
    for r in rocks:
        sum += l - r[0]
    return sum
print(load(rocks))

