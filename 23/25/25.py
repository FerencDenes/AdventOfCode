from collections import defaultdict
input = [ line.split(": ") for line in open('25/input.txt').read().split('\n') ]

graph = defaultdict(set)
for line in input:
    for node in line[1].split(' '):
        graph[node].add(line[0])
        graph[line[0]].add(node)


start = input[0][0]
visited = defaultdict(list)
visited[start] = [start]
queue = [start]
while queue:
    node = queue.pop(0)
    for n in graph[node]:
        if n not in visited:
            visited[n] = visited[node] + [n]
            queue.append(n)

furthest = start
furthestDist = 0
for v in visited:
    if len(visited[v]) > furthestDist:
        furthest = v
        furthestDist = len(visited[v])

for i in range(1,len(visited[furthest])):
    graph[visited[furthest][i]].remove(visited[furthest][i-1])
    graph[visited[furthest][i-1]].remove(visited[furthest][i])

visited = defaultdict(list)
visited[start] = [start]
queue = [start]
while queue:
    node = queue.pop(0)
    for n in graph[node]:
        if n not in visited:
            visited[n] = visited[node] + [n]
            queue.append(n)
for i in range(1,len(visited[furthest])):
    graph[visited[furthest][i]].remove(visited[furthest][i-1])
    graph[visited[furthest][i-1]].remove(visited[furthest][i])

visited = defaultdict(list)
visited[start] = [start]
queue = [start]
while queue:
    node = queue.pop(0)
    for n in graph[node]:
        if n not in visited:
            visited[n] = visited[node] + [n]
            queue.append(n)
for i in range(1,len(visited[furthest])):
    graph[visited[furthest][i]].remove(visited[furthest][i-1])
    graph[visited[furthest][i-1]].remove(visited[furthest][i])

visited = defaultdict(list)
visited[start] = [start]
queue = [start]
while queue:
    node = queue.pop(0)
    for n in graph[node]:
        if n not in visited:
            visited[n] = visited[node] + [n]
            queue.append(n)
print((len(graph) - len(visited)) * len(visited))