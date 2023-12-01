import re
input = [ line for line in open('01/input.txt').read().split('\n') if line != '' ]

print(sum([ int(re.sub(r'^[^0-9]*([0-9]).*', r'\1', line)+re.sub(r'.*([0-9])[^0-9]*$', r'\1', line)) for line in input ]))

# Part 2

input1 = input.copy()
input1 = [ line.replace('oneight', '1ight') for line in input1 ]
input1 = [ line.replace('eightwo', '8wo') for line in input1 ]
input1 = [ line.replace('eighthree', '8hree') for line in input1 ]
input1 = [ line.replace('twone', '2ne') for line in input1 ]

input2 = input.copy()
input2 = [ line.replace('oneight', 'ne8') for line in input2 ]
input2 = [ line.replace('twone', 'tw1') for line in input2 ]
input2 = [ line.replace('eightwo', 'eigh2') for line in input2 ]
input2 = [ line.replace('eighthree', 'eigh3') for line in input2 ]

for i, num in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
    input2 = [ line.replace(num, str(i+1)) for line in input2 ]
    input1 = [ line.replace(num, str(i+1)) for line in input1 ]

for line in input:
    print(line)

print(sum([ int(re.sub(r'^[^0-9]*([0-9]).*', r'\1', line)) for line in input1 ])*10 + sum([ int(re.sub(r'.*([0-9])[^0-9]*$', r'\1', line)) for line in input2 ]))
