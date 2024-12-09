input = [int(c) for c in open('input.txt').read().strip()]
input2 = input.copy()
res1 = 0
i = 0
fn = 0
ind = 0
while i < len(input):
    elem = input[i]
    if i%2 == 0:
        for x in range(elem):
            res1 += fn * ind
            ind += 1
        i += 1
        fn += 1
        continue
    while elem > 0:
        last = input[-1]
        lastFn = len(input) // 2
        if last == 0:
            input.pop()
            input.pop()
            continue
        res1 += lastFn * ind
        ind += 1
        last -= 1
        input[-1] = last
        elem -= 1
    i+=1

print(res1)

# (size, pos)
spaces = []
# (size, fileNo, pos)
files = []
ind = 0
for i in range(len(input2)):
    if i%2 == 1:
        spaces.append((input2[i], ind))
    else:
        files.append((input2[i], i//2, ind))
    ind += input2[i]
res2 = 0
for i in range(len(files)-1, -1, -1):
    fi = files[i]
    moved = False
    for s in range(len(spaces)):
        sp = spaces[s]
        if fi[0] <= sp[0] and sp[1] <= fi[2]:
            moved = True
            spaces[s] = (sp[0] - fi[0], sp[1] + fi[0])
            for x in range(fi[0]):
                res2 += fi[1] * (sp[1] + x)
            spaces.pop()
            break
    if not moved:
        for x in range(fi[0]):
            res2 += fi[1] * (fi[2] + x)
print(res2)