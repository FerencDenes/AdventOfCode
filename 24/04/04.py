import re
input = [line for line in open('input.txt').read().split('\n') ]

def rotate45(matrix):
    ret = []

    for i in range(len(matrix)*2-1):
        str = ""
        for j in range(i, -1, -1):
            if j < len(matrix) and i-j < len(matrix[0]):
                str = str + matrix[j][i-j]
            else:
                str = str + "."
        ret.append(str)
    return ret

def rotate(matrix):
    ret = []
    for i in range(len(matrix)):
        str = ""
        for j in range(len(matrix), -1, -1):
            if j <len(matrix) and i< len(matrix[j]) and matrix[j][i] != ".":
                str = str + matrix[j][i]
        if len(str) > 0:
            ret.append(str)
    return ret
  
xmas = r"XMAS"
def checkXmas(lines):
    res = 0
    for line in lines:
        matches = re.findall(xmas, line)
        res += len(matches)
    return res

def checkMASX(lines):
    res = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "M" and i +2 < len(lines) and j + 2 < len(lines[i]):
                if lines[i+2][j] == "M" and lines[i+1][j+1] == "A" and lines[i][j+2] == "S" and lines[i+2][j+2] == "S":
                    res += 1
    return res
res1 = 0
res2 = 0
for i in range(4):
    res1 += checkXmas(input)
    res2 += checkMASX(input)
    input = rotate45(input)
    res1 += checkXmas(input)
    input = rotate(input)

print(res1)
print(res2)
