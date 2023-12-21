import re
input = [ line for line in open('05/input.txt').read().split('\n') ]

def processSeeds(map, seeds):
    if len(map) == 0:
        return
    map.sort(key=lambda x: x[1])
    for i in range(len(seeds)):
        s = seeds[i]
        # print(seeds[i])
        m = 0
        while m +1< len(map) and map[m+1][1]<=s:
            m += 1
        if m <len(map) and map[m][1] <= s < map[m][1]+map[m][2]:
            s= s-map[m][1]+map[m][0]
        seeds[i] = s
        # print(seeds[i])
        
def processSeeds2(map, seeds):
    ret = []
    if len(map) == 0:
        return seeds
    map.sort(key=lambda x: x[1])
    s = seeds[0]
    i=0
    while i < len(seeds):
        for m in range(len(map)):
            mp = map[m]
            if s[0] >= mp[1]+mp[2]:
                continue
            if map[m][1] <= s[0] < mp[1]+mp[2]:

                trans = (s[0]-mp[1]+mp[0], min(s[1], mp[1]+mp[2]-s[0]))
                ret.append(trans)
                s = (s[0]+trans[1], s[1]-trans[1])
                if 0 == s[1]:
                    break
            elif s[0] <= map[m][1] :
                trans = (s[0], min(s[1], mp[1]-s[0]))
                ret.append(trans)
                s = (s[0]+trans[1], s[1]-trans[1])
                if s[1] == 0:
                    break
        if s[1] <= 0:
            i += 1
            if i < len(seeds):
                s = seeds[i]
        else:
            ret.append(s)
            i += 1
            if i < len(seeds):
                s = seeds[i]
            # ret.append(s)
        # print(seeds[i])
    return ret

seeds = [ int(seed) for seed in input[0].split(': ')[1].split(' ') ]
seeds2 = []
for i in range(0,len(seeds),2):
    seeds2.append((seeds[i], seeds[i+1]))
print(seeds2)
map  = []
for line in input[2:]:
    if 'map' in line or line == '':
        processSeeds(map, seeds)
        seeds2 = processSeeds2(map, seeds2)
        map = []

    else:
        m = [int(v) for v in line.split(' ')]
        map.append(m)

processSeeds(map, seeds)
seeds2 = processSeeds2(map, seeds2)
print(min(seeds))
m = 10000000000000
for s in seeds2:
    if s[0] < m:
        m = s[0]
print(m)

