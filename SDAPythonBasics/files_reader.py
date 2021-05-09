
list_of_content = []

with open('data.txt') as my_file:
    list_of_content = my_file.readlines()

print('My file content is ', list_of_content)

