#Class E
number = int(input('Write a Number: '))
if number > 0:
    raise ValueError

# hint
name = input('What is your name? ')
newfile = open('name', 'a')
for someone in name:

#Home-work:
try:
    a = 1 / 0
except ZeroDivisionError:
    print("You can't division by 0")

words_file = open("E:\Python Projects\words.txt", "x")
my_name = words_file.write("Nadav Chen")
words_file.close()
words_file = open("E:\Python Projects\words.txt", "r")
print(words_file.read())
words_file.close()
words_file = open("E:\Python Projects\words.txt", "a")
words_file.write("זה השם שלי")
words_file.close()
words_file = open("E:\Python Projects\words.txt", "r")
print(words_file.read())
words_file.close()


###################################################################
name_file = open('E:\Python Projects\ names.txt', 'x')
name_list = []
number = 3
with open('E:\Python Projects\ names.txt', 'a') as name_file:
    for name in name_list and number > 0:
        name_file.write(input('What is your name: '))
        number -= 1

with open('E:\Python Projects\ names.txt', 'r') as name_file:
    for name in name_list:
        print(f'Welcome {name}')

name_file = open('E:\Python Projects\ names.txt', 'a')
name1 = input('What is your name: ')
name2 = input('What is your name: ')
name3 = input('What is your name: ')
name_list = [name1, name2, name3]
for name in name_list:
    name_file.write(name)
name_file.close()

name_file = open('E:\Python Projects\ names.txt', 'r')
print(f'''
greetings {name1}
greetings {name2}
greetings {name3}''')
###################################################################
name_file = open(r'E:\Python Projects\names.txt', 'a')
name_list = []
number = 3
while number > 0:
    name_list.append(input('What is your name: '))
    number -= 1
for name in name_list:
    name_file.write(name+"\n")
name_file.close()

name_file = open(r'E:\Python Projects\names.txt', 'r')
content = name_file.read()
content_list = content.splitlines()
for each in content_list:
    print(f'greetings {each}')


# Get a number from the user
# check if it is negative, and if it does throw ValueError exception

try:
    number = int(input('Write a Number: '))
    if number < 0:
        raise ValueError
except ValueError:
    while number < 0:
        print("Error: Negative number, Please enter a number above zero")
        number = int(input('Write a Number: '))


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

##########################
# Creating an Image from the Challenge
from PIL import Image, ImageFont, ImageDraw

name_file = open(r'E:\Python Projects\names.txt', 'a')
name_list = []
number = 3
while number > 0:
    name_list.append(input('What is your name: '))
    number -= 1
for name in name_list:
    name_file.write(name+"\n")
name_file.close()

name_file = open(r'E:\Python Projects\names.txt', 'r')
content = name_file.read()
content_list = content.splitlines()
for each in content_list:
    print(f'greetings {each}')

img = Image.new('RGB',(200,300),color=(62, 50, 168))
draw = ImageDraw.Draw(img)
draw.text((100,100),content,fill=(168, 50, 54))
img.save('Names_Image.png')

###################################################################################################

"""
1. collect what machines to power off
2. state - on or off
3. result status of machines
4. execute action
"""
from time import sleep


ATTEMPTS =5

def _dummy_all_shutdown(machine):
    """
    This is dummy for AWS api to shutdown machine
    :param machine,: this is the lsit of the machines to shuwdown
    :return: State
    """
    print(f"shutting down machines {machine}")

def _dummy_shutdown(machine, wait_for_completion=True, attempts=5):
    """
    This is dummy for AWS api to shutdown machine
    :param machine,: this is the lsit of the machines to shuwdown
    :return: State
    """
    print(f"shutting down machines {machine}")
    if wait_for_completion:
        while _dummy_state(machine) and ATTEMPTS > 0:
            sleep(10)
            attempts -= 1
        raise RuntimeError("The machine was not turned off")
    return True

def _dummy_state(machine):
    """
    This is dummy for AWS api to shutdown machine
    :param machine,: this is the list of the machines to shutdown
    :return: State
    """
    print(f"state of the machines {machine} is true")
    return True

def auto_shutdown(machines_to_shutdown, attempts=5):
    """
    Start the entire shutdown process
    :return:
    """

    for machine in machines_to_shutdown:
        _dummy_all_shutdown(machine)
    for machine in machines_to_shutdown:
        if _dummy_state(machine):
            _dummy_shutdown(machine, wait_for_completion=True, attempts=attempts)

    for machine in machines_to_shutdown:
        if not _dummy_state(machine):
            print(f"the following machine failed to shutdown... {machine}")
