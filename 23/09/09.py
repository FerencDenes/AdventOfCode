input = [ [int(n) for n in line.split(' ')] for line in open('09/input.txt').read().split('\n') ]

def allZero(list):
    for i in list:
        if i != 0:
            return False
    return True
sum =0
sum2=0
for line in input:
    lines = [line]
    while not allZero(lines[len(lines)-1]):
        lines.append([])
        for i in range(len(lines[len(lines)-2])-1):
            lines[len(lines)-1].append(lines[len(lines)-2][i+1] - lines[len(lines)-2][i])
    lines[len(lines)-1].append(0)
    for i in range(len(lines)-1, 0, -1):
        l= lines[i-1]
        nl = lines[i]
        l.append(nl[len(nl)-1]+l[len(l)-1])
    sum += lines[0][len(lines[0])-1]
    n = 0
    for i in range(len(lines)-1, -1, -1):
        n = lines[i][0] - n
    sum2 += n
        
print(sum)
print(sum2)
