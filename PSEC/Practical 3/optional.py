import os
import time

# Constants
SLEEP_DURATION = 1.2
LONGER_SLEEP_DURATION = SLEEP_DURATION + 0.8

# Global lists
list_of_food_dishes = []
ordered_items = []

def clear():
    # Clears screen
    os.system("cls")

def mini_pause():
    # Pauses for 1.2 seconds
    time.sleep(SLEEP_DURATION)

def longer_pause():
    # Pauses for 2 seconds
    time.sleep(LONGER_SLEEP_DURATION)

def pause():
    # Pause program execution till an input is entered
    os.system("pause")

def read_file(fname):
    # Opens filename for reading, entries in the file are split according to newlines, for every entry in the file, add those entries to the global list - list_of_food_dishes
    with open(fname,'r') as f:
        lines = f.read().splitlines()

    for line in lines:
        list_of_food_dishes.append(line)

def order_dishes(temp_dish_list):
    # For use in error checking
    max_dish = len(temp_dish_list)

    while True:
        try:
            clear()
            print("Food to order:")
            print_dishes(temp_dish_list)

            dish_to_order = int(input(f"\nEnter the dish 1-{max_dish} to order, or 0 to stop: "))

            if dish_to_order == 0:  # 9 basically means exit, basically prints out every dish that user has ordered, else, prints an error message saying that user hasn't ordered anything

                if len(ordered_items) > 0:
                    print(f"\nYou have ordered {ordered_items}\n")
                else:
                    print("\nYou have not ordered anything!\n")

                pause()
                break

            elif len(ordered_items) >= 3: # If user ordered 3 or more items, prints an error message and wait for user input, program will loop until user enters '0'

                print("\nYou have ordered 3 items. Please wait for up to 15 minutes")
                pause()

            elif dish_to_order < 1 or dish_to_order > max_dish: # Out of bounds checking to ensure that input is within range

                print(f"\nChosen dish must be between 1 to {max_dish}!")
                mini_pause()    

            else: # If everything goes well, adds the food chosen to the list of ordered items, list index starts with 0, -1 ensures that the food being added to ordered_items list won't match what user has desired and also it prevents out of bounds issues

                dish_to_add = temp_dish_list[dish_to_order - 1]
                ordered_items.append(dish_to_add)

                print(f"\nSucessfully added {dish_to_add} to the list of ordered items!")
                pause()

        except ValueError: # If user entered string instead of numbers
            print("\nDish chosen must be numeric!")
            mini_pause()


def print_dishes(temp_dish_list):
    count = 1 # Initial dish count
    print("") # Print empty line

    for dish in temp_dish_list:
        print(f"{count}) {dish}")
        count += 1 # After printing every element in temp_dish_list, increment count by 1

def search_food(food_to_search):
    global ordered_items # To ensure that we are able to modify global list, this prevents the confusion between global and local level

    similar_dishes = [] # Declares a local list
    ordered_items = []  # CLEARS GLOBAL LIST OF ordered_items

    for food in list_of_food_dishes: # On every iteration, compares both the food to be searched to every element in the list. Here the food to be searched is a substring and element in the list is the full string. If the substring is found in full string, adds the said element(full string) to the list of similar dishes

        tmp = food.lower()

        if tmp.find(food_to_search.lower()) != -1: # Basically means if the substring could be found in a particular string
            similar_dishes.append(food)

    if len(similar_dishes) > 0: # If there are at least 1 similar dishes
        clear()

        print(f"Food similar to {food_to_search}:")
        print_dishes(similar_dishes)

        print("")
        mini_pause()
        clear()

        order_dishes(similar_dishes)
    
    else: # If there are no similar dishes, prints out an error message
        print(f"\nSorry, we don't serve {food_to_search}!")
        print(f"Please choose from {list_of_food_dishes}\n")

        pause()
        clear()

def menu():
    while True:
        clear()
        food_to_search = input("Please input food to search: ").strip()

        if (food_to_search == ""): # If input is empty, it means the user has chosen to exit SPAMS
            print("\nThank you for using SP Automated Menu System(SPAMS)")
            mini_pause()
            clear()
            break

        else:
            if food_to_search.isalpha(): # To limit input to only strings
                search_food(food_to_search)

            else: # If input isn't string, prints out error message
                print("\nPlease enter only strings\n")
                mini_pause()

current_path = os.getcwd()
sub_directory = "\\Practical 3\\"
data_file = "dishes.txt"
full_path = current_path + sub_directory + data_file

read_file(full_path)
clear()
menu()
