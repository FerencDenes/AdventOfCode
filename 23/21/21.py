from collections import defaultdict

input = [ line for line in open('21/input.txt').read().split('\n') ]

def findS():
    for i in range (len(input)):
        for j in range (len(input[i])):
            if input[i][j] == 'S':
                return (i, j)

def part1(num):
    positions = {findS()}

    for s in range(num):
        newPositions = set()
        for p in positions:
            for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newP = (p[0] + dir[0], p[1] + dir[1])
                if newP[0] < 0 or newP[0] >= len(input) or newP[1] < 0 or newP[1] >= len(input[newP[0]]):
                    continue
                if input[newP[0]][newP[1]] == '#' or (newP[0], newP[1]) in positions:
                    continue
                newPositions.add(newP)
        positions = newPositions

    return len(positions)

print(part1(64))

def calculateSteps(stepGoal, grdns, tblsMaps):
    gts = defaultdict(list)
    grdnslist = sorted(list(grdns))
    for g in grdnslist:
        # print(g, end=', ')
        for i in range(len(tblsMaps)):
            t = tblsMaps[i]

            if g in t:
                # print(i, t[g], end=', ')
                gts[g].append(t[g])
        # print()

    print("reach")
    reachPoint = {}
    fullPoint = {}
    for g in grdnslist:
        fullPoint[g] = 10000
        for i in range(len(tblsMaps)):
            t = tblsMaps[i]

            if g in t and g not in reachPoint:
                reachPoint[g] = i
            if g in t and t[g] == 31230:
                fullPoint[g] = i - reachPoint[g]
                break
        # print(g, reachPoint[g], fullPoint[g])
    # print("clusters")
    # gtsDone = set()
    # for g in gts:
    #     if g in gtsDone:
    #         continue
    #     # print(g, end=', ')
    #     maxPoint = g
    #     maxVal = len(gts[g])
    #     for g2 in gts:
    #         if g == g2:
    #             continue
    #         min = len(gts[g])
    #         if len(gts[g2]) < min:
    #             min = len(gts[g2])
    #         if maxVal < len(gts[g2]):
    #             maxVal = len(gts[g2])
    #             maxPoint = g2
    #         if tuple(gts[g][:min]) == tuple(gts[g2][:min]):
    #             print(g2, end=', ')
    #             gtsDone.add(g2)
    #     print()
        
        # for ts in gts[maxPoint]:
        #     if ts == 31230:
        #         break
        #     print(ts, end=', ')
        # print()


    # assume 0,0 is full
    capacity = tbls[(0,0)]
    center = capacity
    # axes
    # (+x,0)
    r1 = (1+ (stepGoal - reachPoint[(1,0)] - fullPoint[(1,0)]) // (reachPoint[(2,0)] - reachPoint[(1,0)]))
    a10 = capacity * r1
    fr = (stepGoal - r1 * (reachPoint[(2,0)] - reachPoint[(1,0)]) - reachPoint[(1,0)])
    for n in range(fr, 0, -(reachPoint[(2,0)] - reachPoint[(1,0)])):
        a10+=gts[(1,0)][(n+1) % fullPoint[(1,0)]]

    # (-x,0)
    r1 = (1+ (stepGoal - reachPoint[(-1,0)] - fullPoint[(-1,0)]) // (reachPoint[(-2,0)] - reachPoint[(-1,0)]))
    na10 = capacity * r1
    fr = stepGoal - r1 * (reachPoint[(-2,0)] - reachPoint[(-1,0)]) - reachPoint[(-1,0)]
    for n in range(fr, 0, -(reachPoint[(-2,0)] - reachPoint[(-1,0)])):
        na10+=gts[(-1,0)][(n+1) % fullPoint[(-1,0)]]

    # (0,+y)
    r1 = (1+ (stepGoal - reachPoint[(0,1)] - fullPoint[(0,1)]) // (reachPoint[(0,2)] - reachPoint[(0,1)]))
    a01 = capacity * r1
    fr = stepGoal - r1 * (reachPoint[(0,2)] - reachPoint[(0,1)]) - reachPoint[(0,1)]
    for n in range(fr, 0, -(reachPoint[(0,2)] - reachPoint[(0,1)])):
        a01+=gts[(0,1)][(n+1) % fullPoint[(0,1)]]
    # (0,-y)
    r1 = (1+ (stepGoal - reachPoint[(0,-1)] - fullPoint[(0,-1)]) // (reachPoint[(0,-2)] - reachPoint[(0,-1)]))
    na01 = capacity * r1
    fr = stepGoal - r1 * (reachPoint[(0,-2)] - reachPoint[(0,-1)]) - reachPoint[(0,-1)]
    for n in range(fr,0, -(reachPoint[(0,-2)] - reachPoint[(0,-1)])):
        na01+=gts[(0,-1)][(n+1) % fullPoint[(0,-1)]]
    
    ln = (stepGoal - reachPoint[(1,1)] - fullPoint[(1,1)])//(reachPoint[(2,1)] - reachPoint[(1,1)]) +1
    pp = capacity * ( ln * (ln+1)/2)
    fr = stepGoal - ln * (reachPoint[(2,1)] - reachPoint[(1,1)]) - reachPoint[(1,1)]
    for n in range(fr, 0, -(reachPoint[(2,1)] - reachPoint[(1,1)])):
        ln+=1
        pp+=gts[(1,1)][(n+1)% fullPoint[(1,1)]] *ln

    ln = (stepGoal - reachPoint[(-1,1)] - fullPoint[(-1,1)])//(reachPoint[(-2,1)] - reachPoint[(-1,1)]) +1
    np = capacity * ( ln * (ln+1)/2)
    fr = stepGoal - ln * (reachPoint[(-2,1)] - reachPoint[(-1,1)]) - reachPoint[(-1,1)]
    for n in range(fr, 0, -(reachPoint[(-2,1)] - reachPoint[(-1,1)])):
        ln+=1
        np+=gts[(-1,1)][(n+1)% fullPoint[(-1,1)]]*ln

    ln = (stepGoal - reachPoint[(1,-1)] - fullPoint[(1,-1)])//(reachPoint[(2,-1)] - reachPoint[(1,-1)]) +1
    pn = capacity * ( ln * (ln+1)/2)
    fr = stepGoal - ln * (reachPoint[(2,-1)] - reachPoint[(1,-1)]) - reachPoint[(1,-1)]
    for n in range(fr, 0, -(reachPoint[(2,-1)] - reachPoint[(1,-1)])):
        ln+=1
        pn+=gts[(1,-1)][(n+1)%fullPoint[(1,-1)]]*ln

    ln = (stepGoal - reachPoint[(-1,-1)] - fullPoint[(-1,-1)])//(reachPoint[(-2,-1)] - reachPoint[(-1,-1)]) +1
    nn = capacity * ( ln * (ln+1)/2)
    fr = stepGoal - ln * (reachPoint[(-2,-1)] - reachPoint[(-1,-1)]) - reachPoint[(-1,-1)]
    for n in range(fr,0, -(reachPoint[(-2,-1)] - reachPoint[(-1,-1)])):
        ln+=1
        nn+=gts[(-1,-1)][(n+1)%fullPoint[(-1,-1)]]*ln

    sum = center + a10 + na10 + a01 + na01 + pp + np + pn + nn
    # print(sum, center, a10, a01, na10, na01, pp , np, pn, nn)
    return sum

positions = {findS()}
tblsMaps = [{}, {(0,0):0}]
grdns = set()
for s in range(1,1100):
    newPositions = set()
    for p in positions:
        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newP = (p[0] + dir[0], p[1] + dir[1])
            if input[newP[0] % len(input)][newP[1] % len(input[0])] == '#' or (newP[0], newP[1]) in positions:
                continue
            newPositions.add(newP)
    positions = newPositions
    tbls = defaultdict(int)
    center = 0
    a10 = 0
    a01 = 0
    na01 = 0
    na10 = 0
    pp = 0
    np = 0
    pn = 0
    nn = 0
    for p in positions:
        xbox = p[0] // (2*len(input))
        ybox = p[1] // (2*(len(input[0])))
        tbls[(xbox,ybox)] += 1
        grdns.add((xbox,ybox))
        if xbox == 0 and ybox == 0:
            center += 1
        elif xbox >0 and ybox == 0:
            a10 += 1
        elif xbox == 0 and ybox > 0:
            a01 += 1
        elif xbox < 0 and ybox == 0:
            na10 += 1
        elif xbox == 0 and ybox < 0:
            na01 += 1
        elif xbox > 0 and ybox > 0:
            pp += 1
        elif xbox < 0 and ybox > 0:
            np += 1
        elif xbox < 0 and ybox < 0:
            nn += 1
        elif xbox > 0 and ybox < 0:
            pn += 1

    tblsMaps.append(tbls)
    print(s, len(positions), center, a10, a01, na10, na01, pp, np, pn, nn)
    # if s > 950:
        # calculateSteps(s, grdns, tblsMaps)
# print(len(positions))
print(calculateSteps(26501365, grdns, tblsMaps))

# reach
# (-2, -1) 395 521
# (-2, 0) 329 456
# (-1, -2) 395 521
# (-1, -1) 133 521
# (-1, 0) 67 456
# (-1, 1) 264 521
# (0, -2) 329 456
# (0, -1) 67 456
# (0, 0) 1 391
# (0, 1) 198 456
# (0, 2) 460 456
# (1, -1) 264 521
# (1, 0) 198 456
# (1, 1) 395 521
# (2, 0) 460 456
# clusters
# (-4, -1), (-3, -2), (-3, -1), (-2, -3), (-2, -2), (-2, -1), (-1, -4), (-1, -3), (-1, -2), (-1, -1), 
# (-4, 0), (-3, 0), (-2, 0), (-1, 0), 
# (-3, 1), (-2, 1), (-2, 2), (-1, 1), (-1, 2), (-1, 3), 
# (0, -4), (0, -3), (0, -2), (0, -1), 
# (0, 0), 
# (0, 1), (0, 2), (0, 3), (0, 4), 
# (1, -3), (1, -2), (1, -1), (2, -2), (2, -1), (3, -1), 
# (1, 0), (2, 0), (3, 0), (4, 0), 
# (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (3, 1), 



# -4, -1) 919 10000
# (-4, 0) 853 10000
# (-4, 1) 1050 10000
# (-3, -2) 919 10000
# (-3, -1) 657 10000
# (-3, 0) 591 456
# (-3, 1) 788 10000
# (-3, 2) 1050 10000
# (-2, -3) 919 10000
# (-2, -2) 657 10000
# (-2, -1) 395 521
# (-2, 0) 329 456
# (-2, 1) 526 521
# (-2, 2) 788 10000
# (-2, 3) 1050 10000
# (-1, -4) 919 10000
# (-1, -3) 657 10000
# (-1, -2) 395 521
# (-1, -1) 133 521
# (-1, 0) 67 456
# (-1, 1) 264 521
# (-1, 2) 526 521
# (-1, 3) 788 10000
# (-1, 4) 1050 10000
# (0, -4) 853 10000
# (0, -3) 591 456
# (0, -2) 329 456
# (0, -1) 67 456
# (0, 0) 1 391
# (0, 1) 198 456
# (0, 2) 460 456
# (0, 3) 722 10000
# (0, 4) 984 10000
# (1, -4) 1050 10000
# (1, -3) 788 10000
# (1, -2) 526 521
# (1, -1) 264 521
# (1, 0) 198 456
# (1, 1) 395 521
# (1, 2) 657 10000
# (1, 3) 919 10000
# (2, -3) 1050 10000
# (2, -2) 788 10000
# (2, -1) 526 521
# (2, 0) 460 456
# (2, 1) 657 10000
# (2, 2) 919 10000
# (3, -2) 1050 10000
# (3, -1) 788 10000
# (3, 0) 722 10000
# (3, 1) 919 10000
# (4, -1) 1050 10000
# (4, 0) 984 10000