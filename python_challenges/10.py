# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated seque
input_numbers_list = input(
    'Please enter the numbers in , separated: ').split(',')
print(','.join([x for x in input_numbers_list if int(x) % 5 == 0]))
