input = [ line for line in open('06/input.txt').read().split('\n') ]

times = [int(x) for x in input[0].split()[1:]]
dists = [int(x) for x in input[1].split()[1:]]
print(times, dists)

# I know I could find the max and the min to win, and all the ones between are fine
# there might also be a closed formula
def findwins(time, dist):
    w =0
    for h in range(time):
        d = (time -h) * h
        if d > dist:
            w += 1
    return w
res =1
for i in range(len(times)):
    res *= findwins(times[i], dists[i])
print(res)

time = int("".join(input[0].split()[1:]))
dist = int("".join(input[1].split()[1:]))
print(findwins(time, dist))
