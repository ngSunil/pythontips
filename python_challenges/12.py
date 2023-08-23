# Write a program that accepts a sentence and calculate the number of letters and digits.
sentence = input('Please enter the sentence: ')
num, chars = 0, 0
for x in sentence:
    if x.isnumeric():
        num += 1
    else:
        chars += 1
print(f'''Number of digits = {num}
Number of characters = {chars}''')
