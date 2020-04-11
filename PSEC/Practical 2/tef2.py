try:
    first_input = int( input("Enter a number: ") )
    second_input = int( input("Enter another number: ") )

    if (first_input > second_input):
        print("\n%d is greater than %d" %(first_input, second_input))
    elif (second_input > first_input):
        print("\n%d is greater than %d" %(second_input, first_input))    
    else:
        print("\n%d is equals to %d" %(first_input, second_input))

except ValueError:
    print("Please enter a valid number!")
