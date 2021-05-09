"""
# Ask the user name/phone cel/phone home/age
# Store those in a dictionary
# Save this dictionary to a list
# and Print out as result this:

[
    {
        'name': 'Aecio',
        'phone_cel': '4535345435',
        'phone_home': '34234234',
        'age': 22
    }
]
"""

list_phone_books = []

name = input("Type your name: ")
phone_cel = input("Type your cel phone number:")
phone_home = input("Type your home number:")
age = input("Type your age:")

phone_book = {}                               # {}

# the syntax to assign a new key and value ( dict_name[KEY] = VALUE )
phone_book['name'] = name                     # {'name': 'Aecio'}
phone_book['phone_cel'] = phone_cel           # {'name': 'Aecio', 'phone_cel': '345435345'}
phone_book['phone_home'] = phone_home         # {'name': 'Aecio', 'phone_cel': '345435345', 'phone_home': '53545435'}
phone_book['age'] = int(age)                       # {'name': 'Aecio', 'phone_cel': '345435345', 'phone_home': '53545435', 'age': 22}

list_phone_books.append(phone_book)           # [{'name': 'Aecio', 'phone_cel': '345435345', 'phone_home': '53545435', 'age': 22}]

print(len(list_phone_books))   # 1
print(list_phone_books)        # [{'name': 'Aecio', 'phone_cel': '345435345', 'phone_home': '53545435', 'age': 22}]



