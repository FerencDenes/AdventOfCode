
from collections import defaultdict
import heapq

input = [[c for c in line.strip()] for line in open('input.txt').readlines()]

for x in range(len(input)):
    for y in range(len(input[x])):
        if input[x][y] == 'S':
            startInit = (x, y)
        if input[x][y] == 'E':
            endInit = (x, y)
def findCosts(start):
    cost = defaultdict(lambda: 10000000000000)
    cost[start] = 0
    heap = [(0, start)]
    while heap:
        c, (x, y) = heapq.heappop(heap)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(input) and 0 <= ny < len(input[nx]) and input[nx][ny] != '#':
                if c + 1 < cost[(nx, ny)]:
                    cost[(nx, ny)] = c + 1
                    heapq.heappush(heap, (c + 1, (nx, ny)))
    return cost
costsSE = findCosts(startInit)
costsES = findCosts(endInit)
fullCost = costsSE[endInit]
def findCheats(length):
    cheats = defaultdict(int)
    for x in range(len(input)):
        for y in range(len(input[x])):
            if input[x][y] == '#':
                continue
            # Check all 4 directions with manhattan distance of length
            for b in range(length):
                for dx, dy in [(b, length - b), (b, -length + b), (-length + b, b), (length - b, b)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(input) and 0 <= ny < len(input[nx]) and input[nx][ny] != '#':
                        newCost = costsSE[(x, y)] + length + costsES[(nx, ny)]
                        if newCost < fullCost and cheats[((x, y),(nx, ny))] < fullCost - newCost:
                            cheats[((x, y),(nx,ny))] = fullCost - newCost
    return cheats
cheats1 = findCheats(2)
res1 = 0
for c in cheats1:
    if cheats1[c] >= 100:
        res1 += 1

print(res1)

def findCheats2(length):
    cheats2 = set()
    for (x1, y1) in costsES:
        for (x2, y2) in costsSE:
            dist= abs(x1 - x2) + abs(y1 - y2)
            if dist <= length:
                newCost = costsSE[(x2, y2)] + dist + costsES[(x1, y1)]
                if newCost <= fullCost -100:
                    cheats2.add(((x2, y2),(x1,y1)))
    return cheats2
cheats2 = findCheats2(20)
print(len(cheats2))
