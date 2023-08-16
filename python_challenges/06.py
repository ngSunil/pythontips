
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 _ C _ D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

import math
inputNum = input('Please enter a number: ')
inputNumToArray = inputNum.split(',')
result = []
c = 50
h = 30


def calc(n):
    return str(math.sqrt((2*c*n)/h))


print(','.join([calc(int(x)) for x in inputNumToArray]))
