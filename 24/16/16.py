import heapq
from collections import defaultdict

input = [[c for c in line.strip()] for line in open("input.txt").readlines()]
dir = (0, 1)
visitedCost = defaultdict(lambda : 100000000000000000000000000)
minCost = 100000000000000000000000000
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == 'S':
            pos = (i, j)
        if input[i][j] == 'E':
            end = (i, j)
visitedCost[(dir, pos)] = 0
reachability = [(0, dir, pos)]
shortest = defaultdict(set)
while len(reachability) > 0:
    nextNode = heapq.heappop(reachability)
    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if dir != nextNode[1] and dir != (-nextNode[1][0], -nextNode[1][1]):
            newCost = nextNode[0] + 1000
            if visitedCost[(dir, nextNode[2])] >= newCost:
                if visitedCost[(dir, nextNode[2])] == newCost:
                    shortest[(dir, nextNode[2])].add((nextNode[1], nextNode[2]))
                else:
                    shortest[(dir, nextNode[2])] = set([(nextNode[1], nextNode[2])])
                visitedCost[(dir, nextNode[2])] = newCost
                heapq.heappush(reachability, (newCost, dir, nextNode[2]))
    newPos = (nextNode[2][0] + nextNode[1][0], nextNode[2][1] + nextNode[1][1])
    if input[newPos[0]][newPos[1]] != '#':
        newCost = nextNode[0] + 1
        if visitedCost[(nextNode[1], newPos)] >= newCost:
            if visitedCost[(nextNode[1], newPos)] == newCost:
                shortest[(nextNode[1], newPos)].add((nextNode[1], nextNode[2]))
            else:
                shortest[(nextNode[1], newPos)] = set([(nextNode[1], nextNode[2])])
            visitedCost[(nextNode[1], newPos)] = newCost
            heapq.heappush(reachability, (newCost, nextNode[1], newPos))
    if nextNode[2] == end:
        if minCost > nextNode[0]:
            minCost = nextNode[0]

print(minCost)
trails = set([end])

unvisitedTrail = set()
for t in visitedCost:
    if visitedCost[t] == minCost and t[1] == end:
        unvisitedTrail.add(t)
while len(unvisitedTrail) > 0:
    nextTrail = unvisitedTrail.pop()
    tr = shortest[nextTrail]
    for t in tr:
        if t not in trails:
            unvisitedTrail.add(t)
            trails.add(t[1])

# for t in trails:
#     input[t[0]][t[1]] = 'O'
# for line in input:
#     print("".join(line))
print(len(trails))

