input = [[int(c) for c in line.strip()] for line in open('input.txt')]
def findReachable(elevation, x, y, results: set):
    if elevation == 9:
        results.add((x, y))
        return 1
    ret = 0
    for p in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        newX = x + p[0]
        newY = y + p[1]
        if newX >= 0 and newX < len(input) and newY >= 0 and newY < len(input[0]) and input[newX][newY] == elevation + 1:
            ret += findReachable(elevation + 1, newX, newY, results)
    return ret
    

res1 = 0
res2 = 0
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == 0:
            results = set()
            pathResults = set()
            res2 += findReachable(0, i, j, results)
            res1 += len(results)
print(res1)
print(res2)