# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a
from functools import reduce

input_digit = input('Please enter a digit: ')
array = []
input_digit1 = input_digit
for x in range(1, int(input_digit)+1):
    input_digit1 = input_digit
    for y in range(1, x):
        input_digit1 += input_digit
    array.append(input_digit1)

print(sum([int(x) for x in array]))
print(reduce(lambda acc, item: acc+item, [int(x) for x in array], 0))
