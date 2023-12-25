import re

input = [ line for line in open('15/input.txt').read().split('\n') ]

strings = input[0].split(',')

def hash(s):
    ret = 0
    for c in s:
        ret += ord(c)
        ret *= 17
        ret %=256
    return ret
sum =0 
for s in strings:
    sum += hash(s)
print(sum)

boxes = []
for i in range(256):
    boxes.append([])
pattern = re.compile(r'(\w+)(.)(.*)')
for s in strings:
    match = pattern.match(s)
    label = match.group(1)
    box = boxes[hash(label)]
    if match.group(2) == '-':
        for i in range(len(box)):
            if box[i][0] == match.group(1):
                box.pop(i)
                break
    elif match.group(2) == '=':
        lens = match.group(3)
        ins = False
        for i in range(len(box)):
            if box[i][0] == match.group(1):
                box[i][1] = lens
                ins = True
                break
        if not ins:
            box.append([label, lens])
sum =0 
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        sum += (i+1)*(j+1)*int(boxes[i][j][1])
print(sum)