starting_number = input("Please enter a starting number: ")

if (starting_number.isdigit()):
    starting_number = int(starting_number)

    ending_number = input("Please enter an ending number: ")

    if(ending_number.isdigit()):
        ending_number = int(ending_number)
        output = "" # For use in storing even numbers

        # Determine even numbers between start and ending range
        for number in range(starting_number, ending_number):
            if (number % 2 == 0):
                output += str(number) + "\t"    # Even numbers separated by tab

        print("\n" + output)   # Prints the total even numbers to the console

    else:
        print("\nEnding number must be numeric")

else:
    print("\nStarting number must be numeric")