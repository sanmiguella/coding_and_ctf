total = 0

# do while in python
while True:
    user_input = input("Please enter a number or Q to stop: ")

    if (user_input == 'Q'):
        print("\nFinal sum is %d" % total)
        break   # Exits while loop
    
    else:
        if (user_input.isdigit()):
            user_input = int(user_input)
            total += user_input
            
            print("\nCurrent total is %d\n" % total)
        
        else:
            print("\nYou didn't enter a number\n")