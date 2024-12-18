import heapq
from collections import defaultdict

input = [[c for c in line.strip()] for line in open("input.txt").readlines()]
print(input)
dir = (0, 1)
visited = defaultdict(lambda : 100000000000000000000000000)
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == 'S':
            pos = (i, j)
        if input[i][j] == 'E':
            end = (i, j)
print(pos, end)
visited[(dir, pos)] = 0
reachability = [(0, dir, pos)]
shortest = defaultdict(set)
while len(reachability) > 0:
    nextNode = heapq.heappop(reachability)
    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if dir != nextNode[1] and dir != (-nextNode[1][0], -nextNode[1][1]):
            if visited[(dir, nextNode[2])] >= nextNode[0] + 1000:
                if visited[(dir, nextNode[2])] == nextNode[0] + 1000:
                    shortest[(dir, nextNode[2])].add(nextNode[1])
                else:
                    shortest[(dir, nextNode[2])] = set([nextNode[1]])
                visited[(dir, nextNode[2])] = nextNode[0] + 1000
                heapq.heappush(reachability, (nextNode[0] + 1000, dir, nextNode[2]))
    newPos = (nextNode[2][0] + nextNode[1][0], nextNode[2][1] + nextNode[1][1])
    if input[newPos[0]][newPos[1]] != '#':
        if visited[(nextNode[1], newPos)] >= nextNode[0] + 1:
            if visited[(nextNode[1], newPos)] == nextNode[0] + 1:
                shortest[(nextNode[1], newPos)].add(nextNode[1])
            else:
                shortest[(nextNode[1], newPos)] = set([nextNode[1]])
            visited[(nextNode[1], newPos)] = nextNode[0] + 1
            heapq.heappush(reachability, (nextNode[0] + 1, nextNode[1], newPos))
    if nextNode[2] == end:
        print(nextNode[0])
        # break
