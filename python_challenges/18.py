# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
user_input = input('Please enter your password? ')

result = []


def checklen(str):
    if len(str) < 6 or len(str) > 12:
        print('Lenght should be between 6 and 12')
        return False
    else:
        return True


def compute(x):
    if (x > 'a' and x < 'z') or (x > 'A' and x < 'Z') or x.isnumeric() or (x in ['$', '#', '@']):
        result.append(True)
        return True
    else:
        return False


if checklen(user_input):
    for x in user_input:
        a = compute(x)
        if not a:
            print('Test failed')
            break
print(result)
