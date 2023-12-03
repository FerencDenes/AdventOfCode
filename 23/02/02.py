import re
input = [ line for line in open('02/input.txt').read().split('\n') if line != '' ]

sum = 0
sum2 = 0
for line in input:
    g, d = line.split(': ')
    ds = re.split(r'[,;] ',d)
    ok = True
    mr = 0
    mg = 0
    mb = 0
    for dd in ds:
        n, c = dd.split(' ')
        if c == 'red':
            if int(n) > 12:
                ok = False
            if mr < int(n):
                mr = int(n)
        if c == 'green':
            if int(n) > 13:
                ok = False
            if mg < int(n):
                mg = int(n)
        if c == 'blue':
            if int(n) > 14:
                ok = False
            if mb < int(n):
                mb = int(n)
    if ok:
        id = int(g.split(' ')[1])
        sum += id
    sum2 += mr * mg * mb
print(sum)

# Part 2
print(sum2)
