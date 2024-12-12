from collections import defaultdict

input = [[c for c in line.strip()] for line in open('input.txt')]

def findFences(x, y):
    points = set()
    unvisitedPoints = set()
    plant = input[x][y]
    unvisitedPoints.add((x, y))
    perimeter = 0
    edgeNum = 0
    sides = defaultdict(list)
    while len(unvisitedPoints) > 0:
        x1, y1 = unvisitedPoints.pop()
        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x2, y2 = x1 + dir[0], y1 + dir[1]
            if x2 < 0 or x2 >= len(input) or y2 < 0 or y2 >= len(input[x2]):
                perimeter += 1
                sides[dir].append((x1, y1))
            elif input[x2][y2] == plant:
                if (x2, y2) not in points:
                    unvisitedPoints.add((x2, y2))
            else:
                perimeter += 1
                sides[dir].append((x1, y1))
        points.add((x1, y1))
    for dir in sides:
        edges = sorted(sides[dir], key=lambda x: x[1]*100000+x[0] if dir[0] == 0 else x[0]*100000+x[1])
        edgeNum += 1
        for i in range(1, len(edges)):
            if dir[0] == 0:
                if abs(edges[i][0] - edges[i - 1][0]) > 1 or edges[i][1] != edges[i - 1][1]:
                    edgeNum += 1
            else:
                if abs(edges[i][1] - edges[i - 1][1]) > 1 or edges[i][0] != edges[i - 1][0]:
                    edgeNum += 1

    for p in points:
        input[p[0]][p[1]] = '.'
    return (perimeter * len(points) , edgeNum * len(points))

res1 = 0
res2 = 0

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] != '.':
            result =  findFences(i, j)
            res1 += result[0]
            res2 += result[1]

print(res1)
print(res2)