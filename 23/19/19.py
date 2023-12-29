import re

input = [ line for line in open('19/input.txt').read().split('\n') ]

wfs = {}
i=0
while True:
    line = input[i]
    i+=1

    if line == '':
        break
    (name, wf) = re.search(r'(.*){(.*)}',line).groups()
    steps = []
    for r in wf.split(','):
        m = re.search(r'([xmas])([<>])(\d+):(.*)',r)
        if m:
            (sub, op, val,dst) = m.groups()
            steps.append((sub, op, int(val), dst))
        else:
            steps.append((r, 'g'))
    wfs[name] = steps

def execute(rule, x, m, a, s):
    for step in rule:
        if step[1] == 'g':
            return step[0]
        if step[0] == 'x':
            targ = x
        elif step[0] == 'm':
            targ = m
        elif step[0] == 'a':
            targ = a
        elif step[0] == 's':
            targ = s
        if step[1] == '<' and targ < step[2]:
            return step[3]
        elif step[1] == '>' and targ > step[2]:
            return step[3]

acc =0
while i < len(input):
    part = input[i]
    (x,m,a,s)= (int(e) for e in re.search(r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}',part).groups())
    wfName = "in"
    while True:
        rule = wfs[wfName]
        wfName = execute(rule, x, m, a, s)
        if wfName == 'A':
            acc += x+m+a+s
            break
        if wfName == 'R':
            break
    i+=1
print(acc)

def findRules(wfName, constraints):
    if wfName == 'A':
        return [constraints]
    if wfName == 'R':
        return []
    rule = wfs[wfName]
    ret = []
    for step in rule:
        if step[1] == 'g':
            cons = constraints.copy()
            dst = step[0]
            r = findRules(dst, cons)
            ret.extend(r)

        elif step[1] == '<':
            val = step[2]
            sub = step[0]
            c = constraints[sub]

            if c[0] < val:
                cons = constraints.copy()
                cons[sub] = (c[0], val)
                r = findRules(step[3], cons)
                ret.extend(r)
            if c[1] <= val:
                break
            constraints[sub] = (val, c[1])
        elif step[1] == '>':
            val = step[2]
            sub = step[0]
            c = constraints[sub]
            if c[1] > val+1:
                cons = constraints.copy()
                cons[sub] = ( val+1, c[1])
                r = findRules(step[3], cons)
                ret.extend(r)
            if c[0] >= val+1:
                break
            constraints[sub] = (c[0], val+1)
    return ret
    

res = findRules('in', {'x':(1,4001),'m':(1,4001),'a':(1,4001),'s':(1,4001)})

borders = {'x':set(),'m':set(),'a':set(),'s':set()}
for r in res:
    for k in r.keys():
        borders[k].add(r[k][0])
        borders[k].add(r[k][1])

for k in borders.keys():
    borders[k] = sorted(list(borders[k]))

sum=0
for ix in range (1, len(borders['x'])):
    px = borders['x'][ix]-borders['x'][ix-1]
    rx = [r for r in res if r['x'][0] <= borders['x'][ix-1] and r['x'][1] >= borders['x'][ix]]
    if len(rx) == 0:
        continue
    for im in range (1, len(borders['m'])):
        pm = (borders['m'][im]-borders['m'][im-1])*px
        rm = [r for r in rx if r['m'][0] <= borders['m'][im-1] and r['m'][1] >= borders['m'][im]]
        if len(rm) == 0:
            continue
        for ia in range (1, len(borders['a'])):
            pa = (borders['a'][ia]-borders['a'][ia-1])*pm
            ra = [r for r in rm if r['a'][0] <= borders['a'][ia-1] and r['a'][1] >= borders['a'][ia]]
            if len(ra) == 0:
                continue
            for i in range (1, len(borders['s'])):
                ps = (borders['s'][i]-borders['s'][i-1])*pa
                rs = [r for r in ra if r['s'][0] <= borders['s'][i-1] and r['s'][1] >= borders['s'][i]]
                if len(rs) == 0:
                    continue
                sum += ps
    
print(sum)