first_input = input("Enter a number: ")

if (first_input.isdigit()):         # Checks if first input is a digit
    second_input = input("Enter another number: ")
    first_input = int(first_input)  # Convert from string to integer

    if (second_input.isdigit()):            # Checks if second input is a digit
        second_input = int(second_input)    # Convert from string to integer

        if (first_input > second_input):
            print("\n%d is greater than %d" %(first_input, second_input))

        elif (second_input > first_input):
            print("\n%d is greater than %d" %(second_input, first_input))

        else:   
            print("\n%d is equals to %d" %(first_input, second_input))

    else:   # Error message
        print("\n%s is not a number" % second_input)

else:       # Error message
    print("\n%s is not a number" % first_input)