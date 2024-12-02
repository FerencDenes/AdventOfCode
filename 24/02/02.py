input = [ [int(x) for x in line.split()] for line in open('input.txt').read().split('\n') ]

def isSafe(path):
    if path[1] == path[0]:
        return False
    prev = path[0]
    incr = (path[1] - path[0])/abs(path[1] - path[0])
    for i in range(1, len(path)):
        diff = path[i] - path[i-1]
        if diff*incr > 3 or diff*incr < 1:
            return False
    return True

safe = 0
remSafe = 0
for i in range(len(input)):
    if isSafe(input[i]):
        safe += 1
        remSafe += 1
    else:
        for j in range(len(input[i])):
            tmpInput = input[i].copy()
            # remove jth element
            tmpInput.pop(j)
            if isSafe(tmpInput):
                remSafe += 1
                break
print(safe)
print(remSafe)
