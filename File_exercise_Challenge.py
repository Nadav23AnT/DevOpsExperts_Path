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