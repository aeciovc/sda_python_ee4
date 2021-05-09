

def my_print(message):   # like print() function
    print(f"This my function! Printing out {message}")

def my_input(msg):
    return 0

def ask_for_value(wish):
    if 'boolean' in wish:
        return True
    elif 'number' in wish:
        return 15
    elif 'string' in wish:
        return 'This is one string'
    else:
        return None

x = input("Type any text:")
my_print(x)

y = my_input("Give me the number!")
print("The number returned was:", y)

value = ask_for_value("give me a boolean!")
print("My value is:", value)

def summ(a, b):
    return a + b

result = summ(3, 2)
print("Sum of two numbers is", result)  # 5

def calculate(number1, number2, operator):
    if '+' in operator:
        return number1 + number2
    elif '-' in operator:
        return number1 - number2
    elif '/' in operator:
        return number1 / number2
    elif '*' in operator:
        return number1 * number2
    else:
        return 'No valid operator!'


result = calculate(2, 2, "*")  # + - / *

print("The result is ", result)   #
