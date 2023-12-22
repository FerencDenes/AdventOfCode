import re
from collections import defaultdict

input = [ line for line in open('08/input.txt').read().split('\n') ]

lr= input[0]

rules = {}
pattern = "(...) = \((...), (...)\)"
for i in range(2,len(input)):
    match = re.match(pattern,input[i])
    
    rules[match.group(1)] = (match.group(2),match.group(3))

def findLength(start, end):
    curr = start
    steps = 0
    while curr != end:
        dir = lr[steps % len(lr)]
        if dir == 'L':
            curr = rules[curr][0]
        else:
            curr = rules[curr][1]
        steps += 1
    return steps

print(findLength("AAA", "ZZZ"))

def findLength2(start):
    curr = start
    steps = 0
    while curr[2] != 'Z':
        dir = lr[steps % len(lr)]
        if dir == 'L':
            curr = rules[curr][0]
        else:
            curr = rules[curr][1]
        steps += 1
    return steps

steps = []
starts = []
for k in rules:
    if k[2] == 'A':
        steps.append(findLength2(k))

sps = {}
for s in steps:
    ps = defaultdict(int)
    sps[s] = ps
    i=2
    while s > 1:
        if s % i == 0:
            ps[i] += 1
            s = s // i
        else:
            i += 1

pps = defaultdict(int)
for s in sps:
    for p in sps[s]:
        pps[p] = max(pps[p], sps[s][p])
prod = 1
for p in pps:
    prod *= p**pps[p]
print(prod)

