from collections import defaultdict

input = open('input.txt').read().strip().split('\n')

points = defaultdict(list)
for i in range(len(input)):
   for j in range(len(input[i])):
      char = input[i][j]
      if char == '.':
         continue
      points[char].append((i, j))

antiNodes = set()
antiNodes2 = set()
for char in points:
   list = points[char]
   for i in range(len(list)):
      for j in range(i + 1, len(list)):
        a = list[i]
        b = list[j]
        maxP = max(a,b)
        minP = min(a,b)
        if minP[1] < maxP[1]:
           antiNodes.add((minP[0] - (maxP[0]-minP[0]), minP[1] - (maxP[1]-minP[1])))
           antiNodes.add((maxP[0] + (maxP[0]-minP[0]), maxP[1] + (maxP[1]-minP[1])))
        else:
            antiNodes.add((minP[0] - (maxP[0]-minP[0]), minP[1] - (maxP[1]-minP[1])))
            antiNodes.add((maxP[0] + (maxP[0]-minP[0]), maxP[1] + (maxP[1]-minP[1])))
        v = (maxP[0] - minP[0], maxP[1] - minP[1])
        for x in range(2, v[0]):
           if v[0]/x == round(v[0]/x) and v[1]/x == round(v[1]/x):
              v = (int(v[0]/x), int(v[1]/x))
        p = a
        while True:
            antiNodes2.add(p)
            p = (p[0] + v[0], p[1] + v[1])
            if not( 0<= p[0] < len(input) and 0<= p[1] < len(input[0])):
               break
        p = a
        while True:
            antiNodes2.add(p)
            p = (p[0] - v[0], p[1] - v[1])
            if not( 0<= p[0] < len(input) and 0<= p[1] < len(input[0])):
               break
              

res1 = sum(1 for i in antiNodes if i[0] >= 0 and i[1] >= 0 and i[0] < len(input) and i[1] < len(input[0]))
print(res1)
print(len(antiNodes2))
