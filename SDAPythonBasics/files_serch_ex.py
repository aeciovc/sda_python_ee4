
name = input("Type username you want to search? ")

with open('user_dict.txt') as f:
    data_str = f.readline()

if data_str == '':
    data_str = '{}'

outer_dict = eval(data_str)

user_details = outer_dict.get(name)

if user_details is None:
    print(f"Sorry, there is no user with this name {name}")
else:
    print(f"Ok, the {name}'s phone number is {user_details.get('phonenumber')} and the city is {user_details.get('city')}")