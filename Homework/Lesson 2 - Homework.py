x = input('Input X:')
y = input('Input Y:')
if x > y:
    print('BIG')
elif x < y:
    print('small')
elif x == y:
    print('Equal')

for num in range(5):
    print(num)

summer = 1
winter = 2
fall = 3
spring = 4
num = input('Please Input a number between 1-4: ')
while not '1' < num < '4':
    num = input('Please! A number between 1-4: ')
if int(num) == 1:
    print('1 = Summer')
elif int(num) == 2:
    print('2 = Winter')
elif int(num) == 3:
    print('3 = Fall')
elif int(num) == 4:
    print('4 = Spring')
while num < '1' or num > '4':
    input('Please! A number between 1-4: ')

age = input('What is your age?')
lastName = input('What is your last name?')
SD = 3.36101691
Flew = input('Did you flew abroad? True or False: ')
Apartment = input('What is you Apartment number? ')
result = SD + int(age)
print(f'Mr {lastName} you are {age},your Apartment number {Apartment}')
print(f'your currency value is {SD} Shekel to Dollar, it is {Flew} that you flew aboard')
print(f'result is: {result}')

count = 1
while count<11:
    print(count)
    count = count + 1

PhoneNumber = input('What is your hone number: ')
print(f'Your Phone Number: {PhoneNumber}')

def printhello():
    name = input('What is your name? ')
    print(f'Your name is: {name}')

def calculate():
    result = 5 + 3.2
    print(result)

def divide2():
    number = input('Write any number: ')
    result = int(number)/2
    print(result)

def sum2():
    number1 = input('Choose a number: ')
    number2 = input('Choose another number: ')
    result = number1 + number2
    return print(result)

def space():
    string1 = input('write something: ')
    string2 = input('write another word: ')
    result = string1 + " " + string2
    return string1 or string2

sign = "#"
sign2 = "#"
for x in sign:
    for x in range(5):
        print(sign)
        sign = sign + sign2


starsize = 7
for x in range(starsize):
    for y in range(starsize):
        if (x == y) or ((starsize - y -1) == x):
            print('*', end = '')
        else:
            print(' ', end = '')
    print('')

def numberlegh():
    num = int(input('Write a Number: '))
    print(num)
    sumit(num)
def sumit(num):
    result = 0
    while num > 0:
        digit = num % 10
        result = result + digit
        num = num // 10
    print(f'sum is: {result}')
numberlegh()
