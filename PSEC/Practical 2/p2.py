import os
import time

def clear():
    os.system("cls")

def pause():
    os.system("pause")

def minor_pause():
    time.sleep(1) # Pause for 1 second

def main_menu():
    try:
        clear()

        print("1. Determine odd or even")
        print("2. Determine bigger number")
        print("3. Find sum of numbers")
        print("4. Display even numbers")
        print("5. Exit")

        choice = int(input("Enter a choice: "))
        return choice

    except ValueError:
        print("\nYou must enter a number.\n")

def odd_or_even():
    try:
        clear()

        user_input = int(input("Enter a number: "))

        if (user_input % 2) == 0:  # No remainder even number
            print("\n%d is an even number.\n" % user_input)
            pause()
            
        else:                     # Any remainder odd number
            print("\n%d is an odd number.\n" % user_input)
            pause()

    except ValueError:
        print("\nOnly numbers should be entered for odd or even game!\n")
        pause()

def bigger_number():
    try:
        clear()

        first_input = int(input("Enter a number: "))
        second_input = int(input("Enter another number: "))

        if (first_input > second_input):
            print("\n%d is bigger\n" % first_input)
            pause()

        elif (second_input > first_input):
            print("\n%d is bigger\n" % second_input)
            pause()

        else:
            print("\n%d and %d are the same!\n" % (first_input, second_input))
            pause()

    except ValueError:
        print("\nEnter only valid number for bigger numbers game!\n")
        pause()

def total_sum():
    count = 0   # For counting the number of valid inputs
    total = 0   # To determine the sum of valid inputs

    # do while in python
    while True:
        clear()

        user_input = input("Please enter a number or Q to stop: ")

        if (user_input == 'Q'):
            average = float(total) / count
            print("\nAverage of %d numbers is %.2f" %(count, average))

            pause()
            break   # Exits while loop

        else:
            if (user_input.isnumeric()):
                count += 1
                total += int(user_input)

                print("\nCurrent total of %d values is %d\n" %(count, total))
                minor_pause()

            else:
                print("\nYou didn't enter a number\n")
                minor_pause()

def display_even():
    try:
        clear()

        start_number = int(input("Enter starting number: "))
        end_number = int(input("Enter ending number: "))
        output = ""

        if (start_number < end_number):
            # For loop increment, lowest to highest
            for number in range(start_number, end_number):
                if (number % 2 == 0):
                    output += str(number) + "\t"

        else:
            # For loop decrement, highest to lowest
            for number in range(start_number -1, end_number, -1):
                if (number % 2 == 0):
                    output += str(number) + "\t"

        print("\n%s\n" % output)
        pause()

    except ValueError:
        print("\nInput must be numeric!\n")
        minor_pause()

while True:
    choice = main_menu()

    if (choice == 1):
        odd_or_even()

    elif (choice == 2):
        bigger_number()

    elif (choice == 3):
        total_sum()

    elif (choice == 4):
        display_even()

    elif (choice == 5):
        print("\nGoodbye!\n")
        minor_pause()
        clear()
        break
