from collections import defaultdict


def encode(s):
    (h,n) = s.split()
    hm = defaultdict(int)
    sum = 0
    sum2= 0
    js=0
    for c in h:
        hm[c] += 1
        if '2'<=c<='9':
            sum += int(c)
            sum2 += int(c)
        elif c == 'T':
            sum += 10
            sum2 += 10
        elif c == 'J':
            sum += 11
            js += 1
        elif c == 'Q':
            sum += 12
            sum2 += 12
        elif c == 'K':
            sum += 13
            sum2 += 13
        elif c == 'A':
            sum += 14
            sum2 += 14
        sum *=100
        sum2 *=100
    max = 0
    maxchar = ''
    for k in hm:
        if k == 'J':
            continue
        if hm[k] > max:
            max = hm[k]
            maxchar = k
    for k in hm:
        sum += 10**hm[k] * 100000000000000000
        if k == 'J':
            continue
        if k == maxchar:
            sum2 += 10**(hm[k]+js) * 100000000000000000
        else:
            sum2 += 10**hm[k] * 100000000000000000
    if h == 'JJJJJ':
        sum2= 10**5 * 100000000000000000
    return (sum, int(n), sum2, h)


input = [ encode(line) for line in open('07/input.txt').read().split('\n') ]

inp = sorted(input)
# print(input)
sum =0
for i in range(len(inp)):
   
   sum += inp[i][1]*(i+1)
print(sum)

inp2 = sorted(input, key=lambda x: x[2])
sum2 = 0
for i in range(len(inp2)):
    sum2 += inp2[i][1]*(i+1)
print(sum2)

        

