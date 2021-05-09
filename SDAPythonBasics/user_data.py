
# Ask the user to enter data and write out his name as capital letters
"""
user_name = input("Enter your name:")

capital = user_name.upper()
print(f"Hello, {capital}!")
"""

# Ask the user to enter a phrase and in the end shows how many letters 'vowels'
# the user typed, no matter if capital or not

user_name = input('Enter your name:')                   # Aecio Costa
user_name_lower = user_name.lower()                     # aecio costa
user_name_replaced = user_name_lower.replace(' ', '')   # aeciocosta

count_a = user_name_lower.count('a')                    # 2
count_e = user_name_lower.count('e')                    # 1
count_i = user_name_lower.count('i')                    # 1
count_o = user_name_lower.count('o')                    # 2
count_u = user_name_lower.count('u')                    # 0

count_sum_vowels = count_a + count_e + count_i + count_o + count_u  # 6
count_sum_consonants = len(user_name_replaced) - count_sum_vowels   # 10 - 6

print(f"Your name '{user_name}' has {count_sum_vowels} vowels and {count_sum_consonants} consonants ")

# Aecio Costa / 6 / 4



