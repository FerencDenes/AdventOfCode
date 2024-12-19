input = [[int(x) for x in line.strip().split(",")] for line in open("input.txt").readlines()]
maxX = 71
maxY = 71

from collections import defaultdict
import heapq
def findPath(corruptionNumber):
    corruptions = {tuple(x) for x in input[:corruptionNumber]}

    visited = defaultdict(int)
    unvisited = []
    unvisitedSet = set()

    heapq.heappush(unvisited, (0, (0, 0)))
    unvisitedSet.add((0, 0))
    while len(unvisited) > 0:
        nextNodeWithCost = heapq.heappop(unvisited)
        dist, node = nextNodeWithCost
        visited[node] = dist
        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nextNode = (node[0] + dir[0], node[1] + dir[1])
            if nextNode[0] < 0 or nextNode[1] < 0 or nextNode[0] >= maxX or nextNode[1] >= maxY:
                continue
            if nextNode in corruptions:
                continue
            if nextNode in visited:
                continue
            if nextNode in unvisitedSet:
                continue
            if nextNode == (maxX - 1, maxY - 1):

                return dist + 1
            heapq.heappush(unvisited, (dist + 1, nextNode))
            unvisitedSet.add(nextNode)
    return -1
print(findPath(1024))
# might have used a binary search
for i in range(1024, len(input)):
    if findPath(i) == -1:
        print(",".join([str(x) for x in input[i-1]]))
        break