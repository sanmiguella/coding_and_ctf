import os
import time

SLEEP_DURATION = 1  # Duration of mini pause

dish_dict = dict()      # Dictionary to store initial food as well as price
ordered_food_list = []  # List to store food which has been ordered

# For use in initially reading the data file that contains food as well as pricing of the said food
current_path = os.getcwd()
subdir = "\\Assignment\\"
data_file = "dishes.txt"
full_path = current_path + subdir + data_file

def clear():
    # Clears screen of any input
    os.system("cls")

def mini_pause():
    # Pause momentarily according to the value defined in the constant SLEEP_DURATION
    time.sleep(SLEEP_DURATION)

def pause():
    # Newline and pause, where program stops until it received a new input
    print("")
    os.system("pause")

def read_data(data_file):
    # File is opened for reading and split according to newlines
    with open(data_file, 'r') as f:
        lines = f.read().splitlines()
    
    # Parsing every line and separating it by using ',' as a delimiter. food is the key while price is the value
    for line in lines:
        food, price = line.split(",")
        dish_dict[food.strip()] = float(price) 

def display_cart():
    # Unformatted printing of the items which has been added to the cart
    clear()
    print(f"In your cart today is {ordered_food_list}")
    pause()

def display_dict():
    clear()

    # Header
    print("=" * 64)
    print("\t\t\tMenu for today")
    print("=" * 64)

    # Food menu starts at 1
    count = 1
    for food in dish_dict:
        food_format = food
        food_format = food_format.ljust(24) # To ensure proper and even formatting of `index. food      :     price` across multiple entries

        print("%s. %s :\t\t$%.2f" %(count, food_format, float(dish_dict[food])))
        count += 1 # If there aren't any increments, index will remain at 1

def tabulate_orders():
    clear()

    unique_list = [] 

    # Given [1, 2, 3, 1, 1]. If 1 is not inside unique_list, adds it as an element to unique_list, else do nothing
    for food in ordered_food_list:
        if food not in unique_list:
            unique_list.append(food)

    # Header
    header_food = "Food".ljust(24)
    print("=" * 64)
    print("%s\tQuantity\tPrice" % header_food)
    print("=" * 64)

    total = 0
    for food in unique_list:
        food_format = food
        food_format = food_format.ljust(24)

        quantity = ordered_food_list.count(food)
        price = quantity * dish_dict[food]
        total += price

        # Food Quantity Price
        # A    x1       $1.20
        print("%s\t%d\t\t$%.2f" %(food_format, quantity, price))

    # Footer
    footer_total = "Total".ljust(24)
    print("-" * 64)
    print("%s\t\t\t$%.2f" %(footer_total, total))
    print("\nThank you for using SPAM. Please pay total of $%.2f" % total)

    pause()
        
def order_food(food_list, price_list):
    global ordered_food_list    # To allow modification of ordered_food_list, else its scope will be local instead of global
    max_dish = len(food_list)

    while True:
        try:
            clear()
            
            count = 0
            print("Yes, we serve the following:\n")

            for food in food_list:
                food_format = food
                food_format = food_format.ljust(24) 

                # 1. Chicken rice : $1.50
                print("%s. %s :\t\t$%.2f" %(count +1, food_format, float(price_list[count])))

                count += 1 # If not index will always remain as 1

            # Only accepts numeric input with try-except block
            choice = int(input(f"\nEnter the dish 1 to {max_dish} that you would like to order, or 0 to stop: "))

            if choice == 0:  
                if len(ordered_food_list) > 0:  # If cart isn't empty, prints out the cart
                    clear()
                    print(f"You have ordered {ordered_food_list}")  
                    pause()

                else:   # If cart is empty, prints out an error message
                    print("\nYou have not ordered anything!")
                    mini_pause()

                break   # Breaks out of the endless while loop to order food and goes back to the main menu

            elif choice < 1 or choice > max_dish:   # Out of bounds checking to prevent choice lesser than 1 or greater than the number of dish being displayed
                print(f"\nChosen dish must be between 1 to {max_dish}!")
                mini_pause()

            else:
                food_choice = food_list[choice -1] # To ensure proper selection because index starts with 0 and not 1
                ordered_food_list.append(food_choice) # Appends the selected food to ordered_food_list

                print(f"\nAdded {food_choice}!")
                mini_pause()

        except ValueError:  # Prints out error if user entered anything besides numeric values
            print("\nOnly numeric values are accepted!")
            mini_pause()

def search_food(food_to_search):
    # List to store the food names and prices of food that is being searched
    similar_dishes_food_list = []
    similar_dishes_price_list = []

    # For every dishes in the dictionary, if the search term matches the key(food name) in the dictionary, program will do 2 things: add the said key to the similar food name list and also add the said value(price) to the similar price list
    for dish in dish_dict:
        # To ensure proper matching regardless of case
        dish_lowercase = dish.lower()
        
        # If the food to be searched is a substring, for example rice is a substring of 'chicken rice'
        if dish_lowercase.find(food_to_search.lower()) != -1:
            similar_dishes_food_list.append(dish)
            similar_dishes_price_list.append(dish_dict[dish])

    # If there are at least 1 similar dish, calls the function to order food and pass the similar_dishes_food_list and similar_dishes_price_list as arguments
    if len(similar_dishes_food_list) > 0:
        order_food(similar_dishes_food_list, similar_dishes_price_list)

    # If there are no similar dishes, prints an error message
    else:
        print(f"\nSorry, we don't serve {food_to_search}!")
        pause()

def search_menu():
    clear()

    # Strips whitespaces we don't want any cases of user unable to search for chicken rice if he accidentally entered ' rice   ' 
    food_to_search = input("Please input food to search or press Enter to go back to the main menu: ").strip()

    if (food_to_search == ""):  # If user doesn't enter anything and press enter, he will be redirected back to the main menu
        print("\nGoing back to the main menu...")
        mini_pause()
    
    else:
        if food_to_search.isalpha():    # More agressive filtering of user input, we dont want user to enter numbers here
            search_food(food_to_search)
        
        else:   # Prints out error message when user
            print("\nPlease enter only strings")
            pause()

def remove_dish_from_cart(selected_dish):
    # Counts the occurences of the selected dish from the ordered_food_list
    quantity = ordered_food_list.count(selected_dish)

    try:
        quantity_to_be_removed = int(input(f"Input the quantity of {selected_dish} to be removed: "))

        if quantity_to_be_removed > quantity:   # If the quantity to be removed is greater than the current quantity in the cart
            print(f"\nYou can only remove a total of {quantity} x {selected_dish} from the cart!")
            pause()

        elif quantity_to_be_removed < 0:    # If the quantity to be removed is lesser than 0
            print("\nNegative values are not accepted!")
            pause()
        
        elif quantity_to_be_removed == 0:   # If user has chosed not to remove any quantity of the selected dish
            print(f"\nYou have chosen not to remove any {selected_dish} from the cart!")
            pause()

        else:
            removed_items = 0
            
            # Loop continues as long as the current count of removed items is not equals to the desired number of items to be removed
            while removed_items < quantity_to_be_removed:
                ordered_food_list.remove(selected_dish)
                removed_items += 1

            print(f"\nRemoved {quantity_to_be_removed} x {selected_dish} from the cart!")
            pause()

    except ValueError:  # If user inputs anything besides numeric values
        print("\nOnly numeric values are accepted!")
        pause()

def add_dish_to_cart(selected_dish):
    try:
        quantity_to_be_added = int(input(f"Input the quantity of {selected_dish} to be added: "))

        if quantity_to_be_added < 0:    # If user inputs negative values
            print("\nNegative values are not accepted!")
            pause()

        elif quantity_to_be_added == 0: # If user chosed not to add any quantity of the selected dish
            print(f"\nYou have chosen not to add any {selected_dish} to the cart!")
            pause()

        else:
            count = 0

            # Loop continues as long as the current count of items to be added is not equals to the desired number of items to be added
            while count < quantity_to_be_added:
                ordered_food_list.append(selected_dish)
                count += 1

            print(f"\nAdded {quantity_to_be_added} x {selected_dish} to the cart!")
            pause()

    except ValueError:
        print("\nOnly numeric values are accepted!")
        pause()

def modify_cart():
    while True:
        try:
            clear()
            unique_list = [] 

            # Given [1, 2, 3, 1, 1]. If 1 is not inside unique_list, adds it as an element to unique_list, else do nothing
            for food in ordered_food_list:
                if food not in unique_list:
                    unique_list.append(food)

            # Header
            header_food = "Food".ljust(24)
            print("=" * 64)
            print("Nr\t%s\tQuantity" % header_food)
            print("=" * 64)

            count = 0
            for food in unique_list:
                food_format = food
                food_format = food_format.ljust(24)

                quantity = ordered_food_list.count(food)

                '''
                Index Food Quantity
                1     A    1 
                '''     
                print("%s\t%s\t%d" %(count +1, food_format, quantity))

                count += 1

            select_food = int(input("\nPlease select the dish number to modify or enter 0 to go back to the main menu: "))

            len_unique_list = len(unique_list)
            
            if select_food == 0:    # Return to main menu
                print("\nReturning back to the main menu")
                mini_pause()
                break

            elif select_food < 1 or select_food > len_unique_list:  # Out of bound error checking to ensure that user only selects food that is being on the menu
                print(f"\nOnly selection 1 to {len_unique_list} are valid!")
                pause()

            else:
                selected_dish = unique_list[select_food -1] # Due to the fact that index starts at 0
               
                clear()
                print(f"1. Remove {selected_dish}")
                print(f"2. Add {selected_dish}")
                modify_choice = int(input("\nChoice: "))

                if modify_choice == 1:
                    clear()
                    remove_dish_from_cart(selected_dish)

                    # If there are no more food in the cart, exits loop
                    if len(ordered_food_list) == 0:
                        clear()
                        print("You have no items in the cart!")
                        pause()
                        break

                elif modify_choice == 2:
                    clear()
                    add_dish_to_cart(selected_dish)

                else:
                    print("\nInvalid input!")
                    mini_pause()

        except ValueError:
            print("\nOnly numeric values are accepted!")
            mini_pause()

def menu():
    clear()

    print("=" * 64)
    print("\t\t\tWelcome to SPAM")
    print("=" * 64)
    print("1. Display Today's Menu")
    print("2. Search Menu")
    print("3. Display Cart")
    print("4. Modify Cart")
    print("5. Check Out")

    choice = input("\nPlease input your choice of action (ENTER to exit): ")
    return(choice)

def start():
    while True:
        choice = menu()

        if (choice == "1"):
            display_dict()
            pause()

        elif (choice == "2"):
            search_menu()

        elif (choice == "3"):
            if len(ordered_food_list) > 0:  # If cart isn't empty, display items in the cart, else prints out an error message
                display_cart()

            else:
                print("\nYou have not ordered anything so menu is not accessible!")
                pause()
        
        elif (choice == "4"):
            if len(ordered_food_list) > 0:
                modify_cart()

            else:
                print("\nYou have not ordered anything so menu is not accessible!")
                pause()

        elif (choice == "5"):
            if len(ordered_food_list) > 0:  # If cart isn't empty, calls a function to display a nice formatted summary of ordered items, else prints out an error message
                tabulate_orders()

            else:
                print("\nYou have not ordered anything so menu is not accessible!")
                pause()

        elif (choice == ""):
            print("\nGoodbye!")
            mini_pause()
            clear()
            break

        else:
            print("\nInvalid input!")
            mini_pause()
            clear()

read_data(full_path)
start()

