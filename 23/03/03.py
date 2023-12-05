input = [ '.'+line+'.' for line in open('03/input.txt').read().split('\n') if line != '' ]
input = ['.'*len(input[0])] + input + ['.'*len(input[0])]

def isSymbol(char):
    return not (char == '.' or '0' <= char <= '9')

def oneIfNum(char):
    if '0' <= char <= '9':
        return 1
    else :
        return 0

sum = 0
for row, line in enumerate(input):
    num = 0
    ok = False
    for col, char in enumerate(line):
        if not('0' <= char <= '9'):
            if ok:
                sum += num
            num = 0
            ok = False
        else :
            num *= 10
            num += int(char)
            if isSymbol(input[row-1][col]) or isSymbol(input[row+1][col]) or isSymbol(input[row][col-1]) or isSymbol(input[row][col+1]) or isSymbol(input[row-1][col-1]) or isSymbol(input[row-1][col+1]) or isSymbol(input[row+1][col-1]) or isSymbol(input[row+1][col+1]):
                ok = True

print(sum)

# Part 2
sum2 = 0
for row, line in enumerate(input):
    for col, char in enumerate(line):
        if char == '*':
            nums = []
            for r in range(row-1, row+2):
                if '0' <= input[r][col-1] <= '9':
                    nums.append(int(input[r][col-1]))
                    c=col-2
                    while '0' <= input[r][c] <= '9':
                        nums[len(nums)-1] += int(input[r][c]) * 10**(col-1-c)
                        c -= 1
                    if '0' <= input[r][col] <= '9':
                        nums[len(nums)-1] *= 10
                        nums[len(nums)-1] += int(input[r][col])
                        if '0' <= input[r][col+1] <= '9':
                            nums[len(nums)-1] *= 10
                            nums[len(nums)-1] += int(input[r][col+1])
                            c = col+2
                            while '0' <= input[r][c] <= '9':
                                nums[len(nums)-1] *= 10
                                nums[len(nums)-1] += int(input[r][c])
                                c += 1
                elif '0' <= input[r][col] <= '9':
                    nums.append(int(input[r][col]))
                    if '0' <= input[r][col+1] <= '9':
                        nums[len(nums)-1] *= 10
                        nums[len(nums)-1] += int(input[r][col+1])
                        c = col+2
                        while '0' <= input[r][c] <= '9':
                            nums[len(nums)-1] *= 10
                            nums[len(nums)-1] += int(input[r][c])
                            c += 1
                if '0' <= input[r][col+1] <= '9' and not '0' <= input[r][col] <= '9':
                    nums.append(int(input[r][col+1]))
                    c = col+2
                    while '0' <= input[r][c] <= '9':
                        nums[len(nums)-1] *= 10
                        nums[len(nums)-1] += int(input[r][c])
                        c += 1

            if len(nums) == 2:
                sum2 += nums[0] * nums[1]
print(sum2)
