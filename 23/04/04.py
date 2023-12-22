import re
input = [ line for line in open('04/input.txt').read().split('\n') if line != '' ]
sum = 0
for line in input:
    c = line.split(':')
    [w, m] = c[1].split('|')
    ws = set(re.split(r' +',w.strip()))
    sc = -1
    for num in re.split(r' +',m.strip()):
        if num in ws:
            sc+=1
    if sc >=0:
        sum += 2**sc
print(sum)

# Part 2
sum2 = [1] * len(input)
res = 0
for i, line in enumerate(input):
    c = line.split(':')
    [w, m] = c[1].split('|')
    ws = set(re.split(r' +',w.strip()))
    sc = 0
    for num in re.split(r' +',m.strip()):
        if num in ws:
            sc+=1
    for j in range(i+1, i+sc+1):
        sum2[j] += sum2[i]
    res += sum2[i]
print(res)