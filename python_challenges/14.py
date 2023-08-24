# Write a program that accepts a sentence and calculate the number of upper case
# letters and lower case letters.
input_string = input('Please enter the string: ')
upper, lower = 0, 0
for x in input_string:
    if x.isupper():
        upper += 1
    elif x.islower():
        lower += 1
print(f'Upper Count {upper} whereas lower count {lower}')
