input = [ line for line in open('11/input.txt').read().split('\n') ]

row = set()
col = set()
gal = set()
for i,line in enumerate(input):
    allDot = True
    for ch in line:
        if ch != '.':
            allDot = False
            break
    if allDot:
        row.add(i)

for i,c in enumerate(input[0]):
    allDot = True
    for line in input:
        if line[i] != '.':
            allDot = False
            break
    if allDot:
        col.add(i)
for i,line in enumerate(input):
    for j,c in enumerate(line):
        if c == '#':
            gal.add((i,j))

sum = 0
sum2 = 0
for (gx,gy) in gal:
    for (g2x,g2y) in gal:
        if gx == g2x and gy == g2y:
            continue
        sum2 += abs(gx-g2x) + abs(gy-g2y)
        sum += abs(gx-g2x) + abs(gy-g2y)

        for i in range(min(gx,g2x), max(gx,g2x)):
            if i in row:
                sum2 += 1000000 -1
                sum+=1
        for r in range(min(gy,g2y), max(gy,g2y)):
            if r in col:
                sum2 += 1000000 -1
                sum+= 1

print(int(sum/2))
print(int(sum2/2))