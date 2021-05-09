
# Receive from user a list of vowels unordered and print out them sorted
"""
vowels = input("Type the vowels")

list_of_vowels = vowels.split(' ')

list_of_vowels.sort()

print("List of vowels: ", list_of_vowels)
"""

# The user will type a letter, is that a vowel?
list_chars = ['a', 'e', 'i', 'o', 'u']
letter = input("Type a letter")

equals = letter in list_chars
print("Result ", equals)

