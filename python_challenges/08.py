# Write a program that accepts a comma separated sequence of words as input
# and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:

print(','.join(sorted(input('Please comma separated words ').split(','))))
