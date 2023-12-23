import re
from collections import defaultdict

input = [ line for line in open('10/input.txt').read().split('\n') ]

spos = (0,0)
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == 'S':
            spos = (i,j)
            break
u = (0,-1)
d = (0,1)
l = (-1,0)
r = (1,0)
curr = (spos[0]-1, spos[1],u)
pipes = {spos, (curr[0], curr[1])}
cnt = 1
while not (curr[0] == spos[0] and curr[1] == spos[1]) or cnt == 1:
    cnt += 1
    if input[curr[0]][curr[1]] == '|':
        if curr[2] == u:
            curr = (curr[0]-1, curr[1], u)
        elif curr[2] == d:
            curr = (curr[0]+1, curr[1], d)
        else:
            print('error')
            break
    elif input[curr[0]][curr[1]] == '-':
        if curr[2] == l:
            curr = (curr[0], curr[1]-1, l)
        elif curr[2] == r:
            curr = (curr[0], curr[1]+1, r)
        else:
            print('error')
            break
    elif input[curr[0]][curr[1]] == 'L':
        if curr[2] == d:
           curr = (curr[0], curr[1]+1, r)
        elif curr[2] == l:
            curr = (curr[0]-1, curr[1], u)
        else:
            print('error')
            break
    elif input[curr[0]][curr[1]] == 'J':
        if curr[2] == d:
            curr = (curr[0], curr[1]-1, l)
        elif curr[2] == r:
            curr = (curr[0]-1, curr[1], u)
        else:
            print('error')
            break
    elif input[curr[0]][curr[1]] == '7':
        if curr[2] == u:
            curr = (curr[0], curr[1]-1, l)
        elif curr[2] == r:
            curr = (curr[0]+1, curr[1], d)
        else:
            print('error')
            break
    elif input[curr[0]][curr[1]] == 'F':
        if curr[2] == u:
            curr = (curr[0], curr[1]+1, r)
        elif curr[2] == l:
            curr = (curr[0]+1, curr[1], d)
        else:
            print('error')
            break
    else:
        print('error')
        break
    pipes.add((curr[0], curr[1]))
print(cnt//2)

inner = 0
for i in range(len(input)):
    isIn = False
    lastB = 'X'
    for j in range(len(input[i])):
        if (i,j) in pipes:
            if input[i][j] == '|' or input[i][j] == 'S':
                isIn = not isIn
                lastB = 'X'
            elif input[i][j] == '7' and lastB == 'L':
                isIn = not isIn
            elif input[i][j] == 'J' and lastB == 'F':
                isIn = not isIn
            elif input[i][j] == 'L':
                lastB = 'L'
            elif input[i][j] == 'F':
                lastB = 'F'
            continue
        if isIn:
            inner += 1
print(inner)
        
