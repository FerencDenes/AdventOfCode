input = [line.strip() for line in open("input.txt").readlines()]

aInit = int(input[0].split(" ")[2])
bInit = int(input[1].split(" ")[2])
cInit = int(input[2].split(" ")[2])

prog = [int(x) for x in input[4].split(" ")[1].split(",")]
def run(a,b,c):
    ret = []
    cnt = 0
    while cnt < len(prog) -1:
        if prog[cnt+1] <= 3:
            op = prog[cnt+1]
        elif prog[cnt+1] == 4:
            op = a
        elif prog[cnt+1] == 5:
            op = b
        elif prog[cnt+1] == 6:
            op = c
        else:
            print("Invalid opcode")
        if prog[cnt] == 0:
            a = a >> op
        elif prog[cnt] == 1:
            b = b ^ prog[cnt+1]
        elif prog[cnt] == 2:
            b = op % 8
        elif prog[cnt] == 3:
            if a != 0:
                cnt = prog[cnt+1] - 2
        elif prog[cnt] == 4:
            b = b ^ c
        elif prog[cnt] == 5:
            ret.append(op % 8)
        elif prog[cnt] == 6:
            b = a >> op
        elif prog[cnt] == 7:
            c = a >> op
        cnt += 2
    return ret


res1 = run(aInit, bInit, cInit)
print(",".join([str(x) for x in res1]))

# while True:
#     b = a % 8
#     b = b ^ 1
#     c = a >> b
#     a = a >> 3
#     b = b ^ 4
#     b = b ^ c
#     print(b%8)
#     if a == 0:
#         break

prob = range(8)
nextprob = []
for n in range(len(prog)-1):
    for i in prob:
        prRes = run(i, 0, 0)
        if prRes == prog[-n-1:]:
            nextprob = nextprob + list(range(i<<3, (i << 3) + 8))
    prob = nextprob
    nextprob = []

for i in prob:
    prRes = run(i, 0, 0)
    if prRes == prog:
        print(i)
        break
