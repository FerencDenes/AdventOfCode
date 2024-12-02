from collections import defaultdict
input = [ line.split() for line in open('input.txt').read().split('\n') ]

a = sorted(map(lambda x:  int(x[0]) , input))
b = sorted(map(lambda x:  int(x[1]) , input))
abssum = 0
for i in range(len(a)):
    abssum += abs(a[i] - b[i])
print(abssum)

numsright = defaultdict(int)
for i in range (len(input)):
    numsright[int(input[i][1])] += 1

similarity = 0
for i in range (len(input)):
    similarity += numsright[int(input[i][0])]*int(input[i][0])

print(similarity)