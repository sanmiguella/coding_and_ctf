import os
import time
from datetime import date
import calendar
import csv

SLEEP_DURATION = 1      # Duration of mini pause

discount_dict = {}      # Dictionary to store discount rates
nested_dish_dict = {}   # Dictionary to store the whole monday to sunday dishes and price
dish_dict = {}          # Dictionary to store initial food as well as price
ordered_food_list = []  # List to store food which has been ordered
discount_rate = 0       # Discount rate in percentage(%)
day_of_the_week = calendar.day_name[date.today().weekday()]

# For use in initially reading the data file that contains food as well as pricing of the said food
current_path = os.getcwd()
subdir = "\\Assignment\\"

data_file = "dishes.csv"
discount_file = "discount.txt"

full_dishes_file_path = current_path + subdir + data_file
full_discount_file_path = current_path + subdir + discount_file

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

def read_data(data_file, arg_dict, option):
    if option == "basic":       # Reading from file to dictionary
        # File is opened for reading and split according to newlines
        with open(data_file, 'r') as f:
            lines = f.read().splitlines()
        
        # Parsing every line and separating it by using ',' as a delimiter.
        for row in lines: 
            name, price = row.split(",")
            arg_dict[name.strip()] = float(price) 

    elif option == "nested":    # Reading from file to nested dictionary
        with open(data_file, 'r') as f:
            data = csv.DictReader(f, delimiter=",")

            for row in data:
                item = arg_dict.get(row["Day"], dict())
                item[row["Dish"]] = float(row["Price"]) # Inner Dictionary
                arg_dict[row["Day"]] = item             # Outer Dictionary 

def display_cart(option):
    clear()

    # https://www.geeksforgeeks.org/python-get-unique-values-list/
    list_set = set(ordered_food_list)
    unique_list = (list(list_set))

    # Header
    header_food = "Food".ljust(24)
    header = f"Nr\t{header_food}\tQuantity\tPrice"
    print_header(header)

    total = 0
    count = 0
    for food in unique_list:
        food_format = food
        food_format = food_format.ljust(24)

        quantity = ordered_food_list.count(food)
        price = quantity * dish_dict[food]
        total += price

        print("%s.\t%s\t%d\t\t$%.2f" % (count +1, food_format, quantity, price))
        count += 1

    # Option to display footer in full which includes total amount
    if option == "full":    
        # Footer
        footer_total = "Total".ljust(24)

        print("-" * 64)
        print("%s\t\t%d\t\t$%.2f" % (footer_total, len(ordered_food_list), total))
        print("-" * 64)

        return total

    # Option to display footer in discount format which includes total, grand total, discounted rate, discounted price
    elif option == "discount":
        # Footer
        footer_total = "Subtotal".ljust(24)
        print("-" * 64)
        print("%s\t\t%d\t\t$%.2f" % (footer_total, len(ordered_food_list), total))

        discounted_price = total * (discount_rate / 100.0)
        footer_total = f"Less {int(discount_rate)}% discount".ljust(24)
        print("%s\t\t\t\t$%.2f" % (footer_total, discounted_price))
        
        grand_total = total * ((100.0 - discount_rate) / 100.0)
        footer_total = "Grand Total".ljust(24)
        
        print("=" * 64)
        print("%s\t\t%d\t\t$%.2f" % (footer_total, len(ordered_food_list), grand_total))
        print("=" * 64)

        print("\nThank you for using SPAM. Please pay a total of ($%.2f)" % grand_total)

    # Option that does not include total, grand total, discounted rate, discounted price
    elif option == "basic":
        print("-" * 64)

def display_food_list(food_list):
    count = 0
    for food in food_list:
        # To ensure proper and even formatting across multiple entries
        food_format = food
        food_format = food_format.ljust(24)

        print("%s. %s :\t\t$%.2f" %(count + 1, food_format, float(dish_dict[food])))
        count += 1  # If there aren't any increments, index will remain at 1

def order_food(food_list, food_being_searched):
    global ordered_food_list    # To allow modification of ordered_food_list, else its scope will be local instead of global
    max_dish = len(food_list)

    while True:
        try:
            clear()          

            header_message = f"Dishes similar to \"{food_being_searched}\""
            print_header(header_message)

            display_food_list(food_list)
            
            # Only accepts numeric input with try-except block
            choice = int(input(f"\nEnter the dish 1 to {max_dish} that you would like to order, or 0 to stop: "))

            if choice == 0:  
                if len(ordered_food_list) > 0:          # If cart isn't empty, prints out the cart
                    clear()
                    display_cart("basic")
                    pause()

                else:   # If cart is empty, prints out an error message
                    print("\nYou have not ordered anything!")

                    mini_pause()

                break   # Breaks out of the endless while loop to order food and goes back to the main menu

            elif choice < 1 or choice > max_dish:       # Out of bounds checking to prevent choice lesser than 1 or greater than the number of dish being displayed
                print(f"\nChosen dish must be between 1 to {max_dish}!")

                mini_pause()

            else:
                food_choice = food_list[choice -1]      # To ensure proper selection because index starts with 0 and not 1
                ordered_food_list.append(food_choice)   # Appends the selected food to ordered_food_list

                print(f"\nAdded [1 x {food_choice}] to the cart!")

                mini_pause()

        except ValueError:  # Prints out error if user entered anything besides numeric values
            print("\nOnly numeric values are accepted!")

            mini_pause()

def search_food(food_to_search):
    # List to store the food names that is being searched
    similar_dishes_food_list = []

    # For every dishes in the dictionary, if the search term matches the key(food name) in the dictionary, program will do 2 things: add the said key to the similar food name list and also add the said value(price) to the similar price list
    for dish in dish_dict:
        # To ensure proper matching regardless of case
        dish_lowercase = dish.lower()
        
        # If the food to be searched is a substring, for example rice is a substring of 'chicken rice'
        if dish_lowercase.find(food_to_search.lower()) != -1:
            similar_dishes_food_list.append(dish)

    # If there are at least 1 similar dish, calls the function to order food and pass the similar_dishes_food_list and similar_dishes_price_list as arguments
    if len(similar_dishes_food_list) > 0:
        order_food(similar_dishes_food_list, food_to_search)

    # If there are no similar dishes, prints an error message
    else:
        print(f"\nSorry, we don't serve {food_to_search}!")

        pause()

def search_menu():
    while True:
        clear()

        # Strips whitespaces we don't want any cases of user unable to search for chicken rice if he accidentally entered ' rice   ' 
        food_to_search = input("Please input food to search or press [Enter] to go back to the main menu: ").strip()

        if (food_to_search == ""):          # If user doesn't enter anything and press enter, he will be redirected back to the main menu
            print("\nGoing back to the main menu...")

            mini_pause()
            
            break
        
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
        quantity_to_be_removed = int(input(f"Input the quantity of [{selected_dish}] to be removed: "))

        if quantity_to_be_removed > quantity:   # If the quantity to be removed is greater than the current quantity in the cart
            print(f"\nYou can only remove a total of [{quantity} x {selected_dish}] from the cart!")

            pause()

        elif quantity_to_be_removed < 0:        # If the quantity to be removed is lesser than 0
            print("\nNegative values are not accepted!")

            pause()
        
        elif quantity_to_be_removed == 0:       # If user has chosed not to remove any quantity of the selected dish
            print(f"\nYou have chosen not to remove any [{selected_dish}] from the cart!")

            mini_pause()

        else:
            removed_items = 0
            
            # Loop continues as long as the current count of removed items is not equals to the desired number of items to be removed
            while removed_items < quantity_to_be_removed:
                ordered_food_list.remove(selected_dish)
                removed_items += 1

            print(f"\nRemoved [{quantity_to_be_removed} x {selected_dish}] from the cart!")

            pause()

    except ValueError:  # If user inputs anything besides numeric values
        print("\nOnly numeric values are accepted!")

        pause()

def add_dish_to_cart(selected_dish):
    try:
        quantity_to_be_added = int(input(f"Input the quantity of {selected_dish} to be added: "))

        if quantity_to_be_added < 0:    # If user inputs negative values
            print("\nNegative values are not accepted!")

            mini_pause()

        elif quantity_to_be_added == 0: # If user chosed not to add any quantity of the selected dish
            print(f"\nYou have chosen not to add any [{selected_dish}] to the cart!")

            mini_pause()

        else:
            # Loop continues as long as the current count of items to be added is not equals to the desired number of items to be added
            count = 0
            while count < quantity_to_be_added:
                ordered_food_list.append(selected_dish)
                count += 1

            print(f"\nAdded [{quantity_to_be_added} x {selected_dish}] to the cart!")

            pause()

    except ValueError:
        print("\nOnly numeric values are accepted!")

        pause()

def modify_cart():
    while True:
        try:
            clear()
            
            # https://www.geeksforgeeks.org/python-get-unique-values-list/
            list_set = set(ordered_food_list)
            unique_list = (list(list_set))

            # Header
            header_food = "Food".ljust(24)
            header = f"Nr\t{header_food}\tQuantity"
            print_header(header)

            count = 0
            for food in unique_list:
                food_format = food
                food_format = food_format.ljust(24)

                quantity = ordered_food_list.count(food)

                print("%s\t%s\t%d" %(count +1, food_format, quantity))
                count += 1
            
            print("-" * 64)

            select_food = int(input("\nPlease select the dish number to modify or enter [0] to go back to the main menu: "))
            
            if select_food == 0:    # Return to main menu
                print("\nReturning back to the main menu")

                mini_pause()

                break

            # Out of bound error checking to ensure that user only selects food that is being on the menu
            elif select_food < 1 or select_food > len(unique_list):
                print(f"\nOnly selection 1 to {len(unique_list)} are valid!")

                mini_pause()

            else:
                selected_dish = unique_list[select_food -1] # Due to the fact that index starts at 0
               
                clear()

                print(f"1. Remove {selected_dish} from the cart")
                print(f"2. Add {selected_dish} to the cart")
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

def print_header(header_message):
    print("=" * 64)
    print(f"{header_message}")
    print("=" * 64)

def menu_discount(): 
    global discount_rate    # To facilitate the change of values of global variable, else scope will be local
    discount_rate = 0       # Resetting discount rate

    clear()

    # Strips off whitespaces and makes it into a lowercase string
    discount_coupon_name = input("Enter name of discount coupon: ").strip().lower()

    coupon_found = False
    for coupon_name in discount_dict: # Case insensitive searching, if the name of the discount coupon matches the coupon name in the dictionary then coupon_found is set to True
        if discount_coupon_name == coupon_name.lower():
            coupon_found = True

    if coupon_found:        # coupon_found means coupon_found == True
        discount_rate = discount_dict[discount_coupon_name]
        print(f"\nThere is a [{int(discount_rate)}%] off purchases for [{discount_coupon_name}] discount coupon!")
        
        pause()
        return(True)
    
    else:
        print(f"\n[{discount_coupon_name}] discount coupon does not exist!")

        pause()
        return(False)

def menu():
    clear()

    print_header("Welcome to SPAM")
    print("1. Display Today's Menu")
    print("2. Search Menu")
    print("3. Display Cart")
    print("4. Modify Cart")
    print("5. Check Out")

    choice = input("\nPlease input your choice of action or press [ENTER] to exit: ")

    return(choice)

def start():
    # To prevent dish_dict from getting a local scope
    global dish_dict
    dish_dict = nested_dish_dict[day_of_the_week]   # Get the dish of the day from the nested dictionary and store it in dish_dist
    
    while True:
        choice = menu()

        if (choice == "1"):
            clear()
            print_header(f"{day_of_the_week}'s Menu")
            display_food_list(dish_dict)
            pause()

        elif (choice == "2"):
            search_menu()

        elif (choice == "3"):
            if len(ordered_food_list) > 0:      # If cart isn't empty, display items in the cart, else prints out an error message
                display_cart("basic")
                pause()

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
            if len(ordered_food_list) > 0:      # If cart isn't empty, calls a function to display a nice formatted summary of ordered items, else prints out an error message
                while True:
                    total = display_cart("full")

                    discount = input("\nThank you for using SPAM. Please pay a total of ($%.2f)\n\nAlternatively, please press 'd' if you have a discount coupon or press [ENTER] to go back to the main menu: " % total)

                    if discount == 'd': # If 'd' was entered, fires up the menu_discount() and gets its return value, if discount exists, shows its result, else, print out the full summary of the cart and prompts for a choice between entering discount or going back to the main menu
                        discount_exist = menu_discount()
                        
                        if discount_exist:  # discount_exist means discount_exist == True
                            display_cart("discount")
                            pause()

                            break
                                            
                    elif discount == "": # Exits back to main menu if user pressed enter
                        break

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

read_data(full_dishes_file_path, nested_dish_dict, "nested")
read_data(full_discount_file_path, discount_dict, "basic")
start()