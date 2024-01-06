import re
import numpy as np
# 176253337504656, 321166281702430, 134367602892386 @ 190, 8, 338
pattern = re.compile(r'(-?\d+),\s*(-?\d+),\s*(-?\d+)\s*@\s*(-?\d+),\s*(-?\d+),\s*(-?\d+)')
input = [ tuple(int(i) for i in re.search(pattern,line).groups()) for line in open('24/input.txt').read().split('\n') ]
testmin = 200000000000000
testmax = 400000000000000
sum =0
for i in range(len(input)-1):
    (x1,y1,z1,t1,u1,v1) = input[i]
   
    for j in range(i+1, len(input)):
        (x2,y2,z2,t2,u2,v2) = input[j]
        # handle parallel lines
        if u2*t1 == u1*t2:
            # print("parallel", i, j)
            if (x1-x2)*u2== (y1-y2)*t2 and (x1-x2)/t2 >=0:
                # print("same line", i, j)
                sum +=1
                continue
            if (x2-x1)*u1 == (y2-y1)*t1 and (x2-x1)/t1 >=0:
                # print("same line", i, j)
                sum +=1
                continue
            continue

        y= (y1*t1-y2*t1 + x2*u1 - x1*u1)/(u2*t1-u1*t2)

        x = (x2+y*t2-x1)/t1
        mx = x2+ y*t2
        my = y2+ y*u2
        # print(i,j, (x1,y1, u1, t1),(x2,y2, u2,v2), (mx,my))

        if y<0 or x<0:
            continue
        if testmin <= mx <= testmax and testmin <= my <= testmax:
            # print("found",i,j)

            sum +=1
print(sum)

# x, y, vx, vy, (xvx - yvy)
A = np.zeros((5,5),dtype=np.int64)
B = np.zeros((5),dtype=np.int64)
for i in range(5):
    A[i,0]= -input[i][4]
    A[i,1]= input[i][3]
    A[i,2]= input[i][1]
    A[i,3]= -input[i][0]
    A[i,4] = 1
    B[i] = -input[i][0]*input[i][4] + input[i][1]*input[i][3]

X = np.linalg.solve(A,B)
print(int(X[0]), int(X[1]), int(X[2]), int(X[3]), int(X[4]))
y= int(X[1])
A = np.zeros((5,5),dtype=np.int64)
B = np.zeros((5),dtype=np.int64)
st = 10
for j in range(st,st+5):
    i = j-st
    A[i,0]= -input[j][3]
    A[i,1]= input[j][5]
    A[i,2]= input[j][0]
    A[i,3]= -input[j][2]
    A[i,4] = 1
    B[i] = input[j][0]*input[j][5] - input[j][2]*input[j][3]

X = np.linalg.solve(A,B)
print(int(X[0]), int(X[1]), int(X[2]), int(X[3]), int(X[4]))


A = np.zeros((5,5),dtype=np.int64)
B = np.zeros((5),dtype=np.int64)
st = 22
for j in range(st,st+5):
    i = j-st
    A[i,0]= -input[j][4]
    A[i,1]= input[j][5]
    A[i,2]= input[j][1]
    A[i,3]= -input[j][2]
    A[i,4] = 1
    B[i] = input[j][1]*input[j][5] - input[j][2]*input[j][4]

X = np.linalg.solve(A,B)
print(int(X[0]), int(X[1]), int(X[2]), int(X[3]), int(X[4]))

z = int(X[0])
# this is not the right number due to nympy's imprecision, however you can pick 2 numbers to form the result
print(x+y+z)
