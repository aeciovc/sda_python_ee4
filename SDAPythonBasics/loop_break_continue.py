
while True:

    continue_in_program = input("Would like to continue using the program? (YES/NO)")

    if continue_in_program.lower() == 'yes':
        continue

    print("I will break the program")
    break

print("The program ended!")
