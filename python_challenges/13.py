# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
input_numbers = input('Please enter the binary numbers comma separated: ')
print(','.join([x for x in input_numbers.split(',') if int(x) % 5 == 0]))
