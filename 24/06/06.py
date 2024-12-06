input = [line for line in open('input.txt').read().split('\n') ]

i=0
j=0
while True:
    for j in range(len(input[0])):
        if input[i][j] == '^':
            break
    if input[i][j] == '^':
        break
    i+=1

startI = i
startJ = j
dir = (-1,0)
steps = set()
steps.add((i,j))
while True:
    np = (i+dir[0], j+dir[1])
    if np[0] < 0 or np[0] >= len(input) or np[1] < 0 or np[1] >= len(input[0]):
        break
    if input[np[0]][np[1]] == '#':
        dir = (dir[1], -dir[0])
    else:
        i= np[0]
        j= np[1]
        steps.add((i,j))

print(len(steps))

res2= 0

for p in steps:
    dir = (-1,0)
    i = startI
    j = startJ
    if p == (i,j):
        continue
    loop = False
    guard = set()
    guard.add((i,j, dir))
    while True:
        np = (i+dir[0], j+dir[1])
        if np[0] < 0 or np[0] >= len(input) or np[1] < 0 or np[1] >= len(input[0]):
            break
        if input[np[0]][np[1]] == '#' or (np[0], np[1]) == p:
            dir = (dir[1], -dir[0])
        else:
            i= np[0]
            j= np[1]
            if (i,j,dir) in guard:
                loop = True
                break
            guard.add((i,j, dir))
    if loop:
        res2+=1
print(res2)