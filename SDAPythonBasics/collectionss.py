# Declare and initialize letter variable
alphabet = ['b', 'c']              # ['b', 'c']

alphabet.append('d')               # ['b', 'c', 'd']

print(f"Content: {alphabet}")

print("2nd position of my list is ", alphabet[1])

special_chars = ["!", "?", ";", "."]
vowels_chars = ['a', 'e', 'i', 'o', 'u']

alphabet.extend(special_chars)  # []
alphabet.extend(vowels_chars)

print("Extended list> ", alphabet)

alphabet.sort()
print(f"Alphabet (sorted): {alphabet} (length: {len(alphabet)})")

# Users
users = ["Alice", "Bob", "Chris", "John"]
print(users)          # ["Alice", "Bob", "Chris", "John"]
print(users[0:3])     # ["Alice", "Bob", "Chris"]
print(users[1:2])     # ["Bob"]
print(users[2])       # Chris
print(users[1:])      # ["Bob", "Chris", "John"]
