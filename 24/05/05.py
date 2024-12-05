from collections import defaultdict
input = [line for line in open('input.txt').read().split('\n') ]

gr = defaultdict(set)
i = 0
while input[i] != '':
    sp = input[i].split('|')
    gr[sp[0]].add(sp[1])
    i += 1

i += 1
res1 = 0
res2 = 0
while i < len(input) and input[i] != '':
    sp = input[i].split(',')
    m = True
    j = 1
    while j < len(sp):
        if sp[j-1] in gr[sp[j]]:
            m = False
            tmp = sp[j]
            sp[j] = sp[j-1]
            sp[j-1] = tmp
            j = 1
        else:
            j += 1
    if m:
        res1 += int(sp[(len(sp)-1)//2])
    else:
        res2 += int(sp[(len(sp)-1)//2])

    i += 1
print(res1)
print(res2)