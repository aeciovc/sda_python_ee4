# Ask the user name/phonenumber/city
# Store his/her data into a file
# The result on this file should be:

#PS: Dont use append mode!

"""
Aecio,545435,Tallinn
Sebastian,6546456,Tallinn
Oskar,43543543,Parnu
"""
list_of_users = []                  # []
name = input('Your name:')
phone = input('Your phone:')
city = input('Your city:')

user_data = f'{name},{phone},{city}\n'  # 'Aecio,4563453,Tallinn'

with open('files_reader_and_writer_ex_data.txt') as file:
    list_of_users = file.readlines()    # ['Sebastian,456346,Tallinn']

list_of_users.append(user_data)         # ['Sebastian,456346,Tallinn', 'Aecio,4563453,Tallinn']

with open('files_reader_and_writer_ex_data.txt', mode='w') as file:
    file.writelines(list_of_users)

print("Thanks, your data has been recorded")
