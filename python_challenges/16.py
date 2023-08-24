# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
print([int(x)**2 for x in input('Please enter the cs numbers: ').split(',') if int(x) % 2 != 0])
