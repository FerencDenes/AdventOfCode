input = [ line for line in open('13/input.txt').read().split('\n') ]

def findS(a):
    ret = None
    for i in range(1,len(a)):
        found = True
        for j in range(min(len(a)-i, i)):
            if a[i+j] != a[i-j-1]:
                found = False
                break
        if found:
            return i
    return ret

p2 = {2**s for s in range( 30)}
def findSmudge(a):
    for i in range(1,len(a)):
        smudged = False
        found = True
        for j in range(min(len(a)-i, i)):
            x = a[i+j] ^ a[i-j-1]
            if not x in p2 and x != 0:
                found = False
                break
            if smudged and x != 0:
                found = False
                break
            if not smudged and x != 0:
                smudged = True
        if found and smudged:
            return i
    return None
            

def findM(arr):
    a = []
    ret = 0
    for l in arr:
        c = 0
        for ch in l:
            c*=2
            if ch == '#':
                c += 1
        a.append(c)
    r = findS(a)
    s1 = findSmudge(a)
    if r != None:
        r= r*100
    if s1 != None:
        s1 = s1*100
    a = []
    for i in range (len(arr[0])):
        c = 0
        for j in range(len(arr)):
            c*=2
            if arr[j][i] == '#':
                c += 1
        a.append(c)
    if r == None:
        r = findS(a)
    if s1 == None:
        s1 = findSmudge(a)
    return (r, s1)

s = 0
s2= 0
arr = []
for line in input:
    res = 0
    if line == '':
        res = findM(arr)
        s += res[0]
        s2 += res[1]
        arr = []
    else:
        arr.append(line)
res = findM(arr)
s += res[0]
s2 += res[1]
print(s)
print(s2)
