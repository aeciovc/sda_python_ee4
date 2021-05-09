

phone_book_dict = {
    'aecio': '33445533',
    'edgar': '8798989'
}

number = phone_book_dict.get('aecio')

print("The number is ", number)

phone_book_dict['kristjan'] = '55665566'

print(phone_book_dict)

#del phone_book_dict['aecio']
phone_book_dict.pop('aecio')

print("After deleting ", phone_book_dict)   #
print(phone_book_dict.get('aecio'))

