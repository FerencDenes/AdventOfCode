
from collections import defaultdict
input = [ line for line in open('23/input.txt').read().split('\n') ]

directed = True

def longestPath(start, end, visited):
    if start == end:
        return len(visited)
    visited.add(start)
    nowadded = [start]
    nexts = [()]
    while len(nexts) == 1 and start != end:
        nexts = []
        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if directed:
                stch = input[start[0]][start[1]]
                if stch == '>' and dir != (0, 1):
                    continue
                if stch == '<' and dir != (0, -1):
                    continue
                if stch == '^' and dir != (-1, 0):
                    continue
                if stch == 'v' and dir != (1, 0):
                    continue

            s1 = start[0] + dir[0]
            s2 = start[1] + dir[1]
            if s1 < 0 or s1 >= len(input) or s2 < 0 or s2 >= len(input[s1]) or (s1, s2) in visited:
                continue
            ch = input[s1][s2]
            if ch == '#':
                continue
            nexts.append((s1, s2))
        if len(nexts) == 1:
            visited.add(nexts[0])
            start = nexts[0]
            nowadded.append(start)
        elif len(nexts) == 0:
            for n in nowadded:
                visited.remove(n)
            return 0
    
    if start == end:
        l= len(visited)
        for n in nowadded:
            visited.remove(n)
        return l
    max = 0
    for n in nexts:
        l = longestPath(n, end, visited)
        if l > max:
            max = l
    if len(visited) > max and start == end:
        max = len(visited)
    for n in nowadded:
        visited.remove(n)
    return max

for i in range(len(input[0])):
    if input[0][i] == '.':
        start= (0, i)
        break
for i in range(len(input[-1])):
    if input[-1][i] == '.':
        end= (len(input) - 1, i)
        break
print(longestPath(start, end, set())-1)

graph = defaultdict(set)
visited = set()
def buildGraph():
    tovisit = {(start, (1, start[1]))}
    while len(tovisit) > 0:
        (st, n) = tovisit.pop()
        visited.add((st,n))
        cnt = 0
        nexts = [()]
        prev = st
        curr = n
        while len(nexts) == 1:
            nexts = []
            cnt += 1
            for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                s1 = curr[0] + dir[0]
                s2 = curr[1] + dir[1]
                if s1 < 0 or s1 >= len(input) or s2 < 0 or s2 >= len(input[s1]) or prev == (s1, s2):
                    continue
                ch = input[s1][s2]
                if ch == '#':
                    continue
                nexts.append((s1, s2))
            if len(nexts) == 1:
                prev = curr
                curr = nexts[0]
        if len(nexts) == 0 and curr != end:
            continue
        for n in nexts:
            if (curr,n) in visited:
                continue
            tovisit.add((curr,n))
        graph[st].add((curr, cnt))
        graph[curr].add((st, cnt))

buildGraph()

def longestGraph(start, visited):
    if start == end:
        return 0
    visited.add(start)
    max = -100000000000
    fwd = False
    for n in graph[start]:
        if n[0] in visited:
            continue
        fwd = True
        l = longestGraph(n[0], visited) +n[1]
        if l > max:
            max = l
    visited.remove(start)
    return max

print(longestGraph(start, set()))