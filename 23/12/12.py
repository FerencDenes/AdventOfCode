input = [ line for line in open('12/input.txt').read().split('\n') ]

memo = {("", ()): 1}
def fit(m, n):
    if (m, n) in memo:
        return memo[(m, n)]
    ret = 0
    if (sum(n) + len(n) - 1 > len(m)):
        memo[(m, n)] = 0
        return 0
    if m[0] != '#':
        ret = fit(m[1:], n)
    if m[0] != '.' and len(n) > 0:
        all = True
        for i in range(n[0]):
            if m[i] == '.':
                all = False
                break
        if all:
            if len(m) == n[0] and len(n) == 1:
                ret += 1
            elif len(m) >= n[0] + 1 and m[n[0]] != '#':
                ret += fit(m[n[0]+1:], n[1:])
    memo[(m, n)] = ret
    return ret                

s =0 
for line in input:
    (m, tmp) = line.split(' ')
    n = [ int(v) for v in tmp.split(',') ]
    s+= fit(m, tuple(n))
    
print(s)
s2=0
i = 0
for line in input:
    i+=1
    (m, tmp) = line.split(' ')
    n = [ int(v) for v in tmp.split(',') ] *5
    m= m +'?' + m + '?' + m + '?' + m + '?' +m
    f= fit(m, tuple(n))
    s2+= f
print(s2)