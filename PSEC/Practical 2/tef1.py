try:
    user_input = int( input("Enter a number: ") )

    if (user_input % 2) == 0: # No remainder even number
        print("\n%d is an even number." % user_input)
    else:                     # Any remainder odd number
        print("\n%d is an odd number." % user_input)

except ValueError:
    print("\nPlease enter a valid number!")