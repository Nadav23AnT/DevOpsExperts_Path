#                     Question number 1
try:
    name_file = open(r'E:\Python Projects\names.txt', 'a')
except FileNotFoundError:
    print("Sorry this file doesn't exist")
name_list = []
number = 3
while number > 0:
    name_list.append(input('What is your name: '))
    number -= 1
for name in name_list:
    name_file.write(name+"\n")
name_file.close()

try:
    name_file = open(r'E:\Python Projects\names.txt', 'r')
except FileNotFoundError:
    print("Sorry this file doesn't exist")
content = name_file.read()
content_list = content.splitlines()
for each in content_list:
    print(f'greetings {each}')

#                     Question number 2 + 3

try:
    number = int(input('Write a Number: '))
    if number < 0:
        raise ValueError
except ValueError:
    while number < 0:
        print("Error: Negative number, Please enter a number above zero")
        number = int(input('Write a Number: '))

