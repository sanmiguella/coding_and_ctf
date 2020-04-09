user_input = input("Enter a number: ")  # Gets input from user

if (user_input.isdigit()) :
    user_input = int(user_input)        # Type conversion from string to integer

    if (user_input % 2) == 0:           # If remainder is 0, the input is an even number
        print("%d is an even number." % user_input)
    else:                               # If remainder is anything other than 0, it is an odd number
        print("%d is an odd number." % user_input)
else:
    print("You did not enter a number.")