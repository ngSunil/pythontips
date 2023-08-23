# Write a program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
result_array = []
for y in range(1000, 3001):
    flag = ''
    for x in str(y):
        if int(x) % 2 != 0:
            flag = 'odd'
    if flag != 'odd':
        result_array.append(str(y))
print(','.join(result_array))
