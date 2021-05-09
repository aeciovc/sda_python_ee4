name = input("Type your name:")
phonenumber = input("type your phone:")
city = input("type your city:")

inner_dict = {
    'phonenumber': phonenumber,
    'city': city
}

with open('user_dict.txt') as f:
    data_str = f.readline()

if data_str == '':
    data_str = '{}'

outer_dict = eval(data_str)

outer_dict[name] = inner_dict

with open('user_dict.txt', mode='w') as file:
    file.write(str(outer_dict))
