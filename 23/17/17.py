input = [ [int(l) for l in line] for line in open('17/input.txt').read().split('\n') ]
l = 0
r = 1
d = 2
u = 3

def part1():
    st =3   # straight
    # pos, dir, straight steps => cost
    visited = {}
    tovisit = [(0,0,1,0,0)]

    def stepnext(x, y, dir, straight, cost):
        c = visited.get((x,y,dir,straight))
        if c == None or c > cost:
            # visited[(x,y,dir,straight)] = cost
            tovisit.append((x,y,dir,straight,cost))

    step = 0
    mx = 0
    my =0
    mm = 0
    while len(tovisit) > 0:
        step += 1
        (x,y,dir,straight, cost) = tovisit.pop(0)
        if mx < x:
            mx = x
        if my < y:
            my = y
        if mm < x+y:
            mm = x+y
        v=visited.get((x,y,dir,straight))
        if (v!= None and v <= cost):
            continue
        visited[(x,y,dir,straight)] = cost

        # for s in range(straight+1, st+1):
        #     v=visited.get((x,y,dir,s))
        #     if (v== None or v > cost):
        #         visited[(x,y,dir,s)] = cost
        
        if dir == l:
            if straight < st and x > 0:
                stepnext(x-1,y,l,straight+1, cost+input[x-1][y])
            if y > 0:
                stepnext(x,y-1,u,1, cost+input[x][y-1])
            if y < len(input[0])-1:
                stepnext(x,y+1,d,1, cost+input[x][y+1])
        elif dir == r:
            if straight < st and x < len(input)-1:
                stepnext(x+1,y,r,straight+1, cost+input[x+1][y])
            if y > 0:
                stepnext(x,y-1,u,1, cost+input[x][y-1])
            if y < len(input[0])-1:
                stepnext(x,y+1,d,1, cost+input[x][y+1])
        elif dir == u:
            if straight < st and y > 0:
                stepnext(x,y-1,u,straight+1, cost+input[x][y-1])
            if x > 0:
                stepnext(x-1,y,l,1, cost+input[x-1][y])       
            if x < len(input)-1:
                stepnext(x+1,y,r,1, cost+input[x+1][y])
        elif dir == d:
            if straight < st and y < len(input[0])-1:
                stepnext(x,y+1,d,straight+1, cost+input[x][y+1])
            if x > 0:
                stepnext(x-1,y,l,1, cost+input[x-1][y])
            if x < len(input)-1:
                stepnext(x+1,y,r,1, cost+input[x+1][y])
        print(len(tovisit), len(visited), step, mx, my, mm)

    # print(visited[(len(input)-1, len(input[0])-1, r, 1)])
    min = 1000000000000
    for i in range(5):
        for j in range(5):
            c = visited.get((len(input)-1, len(input[0])-1, i, j))
            if c != None and c < min:
                print(i,j,c)
                min = c
    print(min)

part1()
def part2():
    visited = {}
    tovisit = {(0,0,0,0)}

    def stepnext(x, y, dir, cost):
        c = visited.get((x,y,dir))
        if c == None or c > cost:
            tovisit.add((x,y,dir,cost))

    def stepToDir(x, y, dir, cost):
        if dir == l:
            c = cost
            for i in range(1,11):
                if x-i >= 0:
                    c+=input[x-i][y]
                    if i >= 4:
                        stepnext(x-i,y,l,c)
        if dir == r:
            c = cost
            for i in range(1,11):
                if x+i < len(input):
                    c+=input[x+i][y]
                    if i >= 4:
                        stepnext(x+i,y,r,c)
        if dir == u:
            c = cost
            for i in range(1,11):
                if y-i >= 0:
                    c+=input[x][y-i]
                    if i >= 4:
                        stepnext(x,y-i,u,c)
        if dir == d:
            c = cost
            for i in range(1,11):
                if y+i < len(input[0]):
                    c+=input[x][y+i]
                    if i >= 4:
                        stepnext(x,y+i,d,c)

    step = 0
    mx = 0
    my =0
    mm = 0
    while len(tovisit) > 0:
        step += 1
        (x,y,dir, cost) = tovisit.pop()
        if mx < x:
            mx = x
        if my < y:
            my = y
        if mm < x+y:
            mm = x+y
        v=visited.get((x,y,dir))
        if (v!= None and v <= cost):
            continue
        visited[(x,y,dir)] = cost
        
        if dir == l:
            stepToDir(x,y,u,cost)
            stepToDir(x,y,d,cost)
        elif dir == r:
            stepToDir(x,y,u,cost)
            stepToDir(x,y,d,cost)
        elif dir == u:
            stepToDir(x,y,l,cost)
            stepToDir(x,y,r,cost)
        elif dir == d:
            stepToDir(x,y,l,cost)
            stepToDir(x,y,r,cost)
        # print(len(tovisit), len(visited), step, mx, my, mm)
    min = 1000000000000
    for i in range(5):
        c = visited.get((len(input)-1, len(input[0])-1, i))
        if c != None and c < min:
            min = c
    print(min)


part2()