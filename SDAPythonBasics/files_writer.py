
list_of_name = [
    'Aecio', 'Vee', 'Oskar'
]

with open('data.txt', mode='w') as my_file:
    my_file.writelines(list_of_name)

print("The data has been recorded!")