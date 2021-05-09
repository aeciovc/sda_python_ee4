"""
Write a program that based on the variable temperature in degrees Celsius - temp_in_Celsius (float),
will calculate the temperature in degrees Farhenheit (degrees Fahrenheit = 1.8 * degrees Celsius + 32.0)
and write it in the console.

Get the temperature from the user in the console using argument-less input().
"""
celsius_str = input("Type the temperature in Celsius:")

celsius = float(celsius_str)

fahrenheit = 1.8 * celsius + 32.0

print(f"The temperature in Celsius {celsius}, it is in Fahrenheit {fahrenheit}")
