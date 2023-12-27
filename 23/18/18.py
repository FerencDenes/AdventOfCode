
import re
from collections import defaultdict

input = [ re.search(r'(.) (\d*) \(\#(.+)\)',line).groups() for line in open('18/input.txt').read().split('\n') ]

pos = (0,0)
dig = {pos}
for d in input:
    if d[0] == 'D':
        for i in range(int(d[1])):
            pos = (pos[0], pos[1]+1)
            dig.add(pos)
    elif d[0] == 'U':
        for i in range(int(d[1])):
            pos = (pos[0], pos[1]-1)
            dig.add(pos)
    elif d[0] == 'L':
        for i in range(int(d[1])):
            pos = (pos[0]-1, pos[1])
            dig.add(pos)
    elif d[0] == 'R':
        for i in range(int(d[1])):
            pos = (pos[0]+1, pos[1])
            dig.add(pos)

toVisit = {(1,1)}
while len(toVisit) > 0 :
    visited = toVisit.pop()
    if visited in dig:
        continue
    dig.add(visited)
    toVisit.add((visited[0]+1, visited[1]))
    toVisit.add((visited[0]-1, visited[1]))
    toVisit.add((visited[0], visited[1]+1))
    toVisit.add((visited[0], visited[1]-1))
print(len(dig))

pos = (0,0)
trench = defaultdict(list)
horarea = 0

for d in input:
    l = int(d[2][:5], 16)
    dir = d[2][5]
    if dir == '0':
        newPos = (pos[0], pos[1]+l)
        horarea += l
    elif dir == '1':
        newPos = (pos[0]+l, pos[1])
    elif dir == '2':
        newPos = (pos[0], pos[1]-l)
    elif dir == '3':
        newPos = (pos[0]-l, pos[1])
    trench[pos].append(newPos)
    trench[newPos].append(pos)
    pos = newPos

trench[(0,0)] = [trench[(0,0)][1], trench[(0,0)][0]]

area = 0

points = []
for p in trench:
    points.append(p)
points.sort()

borders = [points[0],points[1]]
prev = points[1][0]
i=1
while i < len(points) -1:
    i+=1
    p = points[i]
    if prev < points[i][0]:
        borders.sort(key=lambda x: x[1])
        for j in range(0,len(borders),2):
            area += (borders[j+1][1]-borders[j][1]+1)*(points[i][0] - prev)
        prev = points[i][0]
    borders.append(points[i])
    for j in range(len(borders)-1,-1,-1):
        b = trench[borders[j]]
        if b[0][0] <= prev and b[1][0] <= prev:
            borders.pop(j)

print(area+horarea+1)      
