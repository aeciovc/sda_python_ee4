"""
Write a program that takes from the user two integers A - a (int) and B - b (int),
where A < B, and then calculates the sum of the sequence of numbers from A to B (A, A + 1, A + 2, ..., B)
and prints it in the console.

When the A < B condition is not met,the program exits by writing Job finished in the console.

For example, for A = 4 and B = 11, the program should write the number 60 in the console.

Get data from the user in the console using argument-less input().
"""
a = int(input("Type number 1:"))
b = int(input("Type number 2:"))

if b <= a:
    print("Job finished!")
    exit()

sum = 0
for i in range(a, b + 1):
    sum = sum + i

print(f"Sum of the numbers from {a} to {b} is {sum}")