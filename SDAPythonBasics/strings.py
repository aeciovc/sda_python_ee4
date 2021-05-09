# Prints the number of characters in the sequence
sentence = "Lorem ipsum dolor sit amet..."

amount = len(sentence)
print(amount)  # Prints 29

hello = "Hello, World!"

amount_app = hello.count('o', 0, 8)
print(amount_app)  # Prints 4


# List and strings
list_of_letters = ['A', 'E', 'C', 'I', 'O']
string_of_letters = 'AECIO'

name = 'Aecio Costa'

name1 = 'A'
age = 1

print(f" The type for string_of_letters is {type(string_of_letters)}")
print(f" The type for list_of_letters is {type(list_of_letters)}")

index = 0

print(string_of_letters[index], end='!')
print(string_of_letters[1], end='!')
print(string_of_letters[2], end='!')
print(string_of_letters[3], end='')
print(string_of_letters[4])

print(list_of_letters[0])

#
start = 7
stop = 12
step = 2

hello = "Hello, World!"
print(hello[start:len(hello):step])

# Upper
hello = "Hello, World!"
print(hello.upper()) # Prints HELLO, WORLD!