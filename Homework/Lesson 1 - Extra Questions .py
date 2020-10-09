Name = input('What is your name?')
Age = input('And how old are you?')
Work = input('what do you do for a living?')
while not Name.startswith('A'):
    Name = input('What is your name Please?')
if Name.startswith('A'):
    if int(Age):
        print(f'Yes! your age is {Age}')
    else:
        print("You didn't wrote a number")
