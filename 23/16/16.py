import copy
# right, down, left, up
r= 1
d =2
l = 3
u = 4
input = [ [[c,False,False,False,False] for c in line] for line in open('16/input.txt').read().split('\n') ]

def energized(x,y,dir, input):
    toVisit = {(x ,y, dir)}

    while len(toVisit) >0:
        visited = toVisit.pop()
        v = input[visited[0]][visited[1]]
        if v[visited[2]]:
            continue
        v[visited[2]] = True
        if visited[2] == r:
            if (v[0] == '.' or v[0] == '-') and visited[1] < len(input[0])-1:
                toVisit.add((visited[0], visited[1]+1, r))
            elif v[0] == '/' and visited[0] > 0:
                toVisit.add((visited[0]-1, visited[1], u))
            elif v[0] == '\\' and visited[0] < len(input)-1:
                toVisit.add((visited[0]+1, visited[1], d))
            elif v[0] == '|':
                if visited[0] > 0:
                    toVisit.add((visited[0]-1, visited[1], u))
                if visited[0] < len(input)-1:
                    toVisit.add((visited[0]+1, visited[1], d))
        elif visited[2] == d:
            if (v[0] == '.' or v[0] == '|') and visited[0] < len(input)-1:
                toVisit.add((visited[0]+1, visited[1], d))
            elif v[0] == '/' and visited[1] > 0:
                toVisit.add((visited[0], visited[1]-1, l))
            elif v[0] == '\\' and visited[1] < len(input[0])-1:
                toVisit.add((visited[0], visited[1]+1, r))
            elif v[0] == '-':
                if visited[1] > 0:
                    toVisit.add((visited[0], visited[1]-1, l))
                if visited[1] < len(input[0])-1:
                    toVisit.add((visited[0], visited[1]+1, r))
        elif visited[2] == l:
            if (v[0] == '.' or v[0] == '-') and visited[1] > 0:
                toVisit.add((visited[0], visited[1]-1, l))
            elif v[0] == '/' and visited[0] < len(input)-1:
                toVisit.add((visited[0]+1, visited[1], d))
            elif v[0] == '\\' and visited[0] > 0:
                toVisit.add((visited[0]-1, visited[1], u))
            elif v[0] == '|':
                if visited[0] > 0:
                    toVisit.add((visited[0]-1, visited[1], u))
                if visited[0] < len(input)-1:
                    toVisit.add((visited[0]+1, visited[1], d))
        elif visited[2] == u:
            if (v[0] == '.' or v[0] == '|') and visited[0] > 0:
                toVisit.add((visited[0]-1, visited[1], u))
            elif v[0] == '/' and visited[1] < len(input[0])-1:
                toVisit.add((visited[0], visited[1]+1, r))
            elif v[0] == '\\' and visited[1] > 0:
                toVisit.add((visited[0], visited[1]-1, l))
            elif v[0] == '-':
                if visited[1] > 0:
                    toVisit.add((visited[0], visited[1]-1, l))
                if visited[1] < len(input[0])-1:
                    toVisit.add((visited[0], visited[1]+1, r))

    sum = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j][4]  or input[i][j][1] or input[i][j][2] or input[i][j][3]:
                sum += 1
    return sum

print(energized(0,0,r,copy.deepcopy(input)))

max = 0
for i in range(len(input)):
    res = energized(i,0,r,copy.deepcopy(input))
    if res > max:
        max = res
    res = energized(i,len(input[0])-1,l,copy.deepcopy(input))
    if res > max:
        max = res

for i in range(len(input[0])):
    res = energized(0,i,d,copy.deepcopy(input))
    if res > max:
        max = res
    res = energized(len(input)-1,i,u,copy.deepcopy(input))
    if res > max:
        max = res
print(max)