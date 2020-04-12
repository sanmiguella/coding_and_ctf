import os
import time

# Constant for time.sleep()
SLEEP_DURATION = 1.2

# List in global scope which is accessible to all functions
marks = []

def clear():
    # To clear screen, provides a more better visual experience
    os.system("cls")

def pause():
    # No further action unless any other key is pressed
    os.system("pause")

def mini_pause():
    # Pause for a short time
    time.sleep(SLEEP_DURATION)

def display_marks():
    # If marks list isn't empty, display all the elements in the list
    if (len(marks) > 0):
            print("Current marks for %d students stored in system." % len(marks))
            print(marks)

def max_marks():
    # If marks list isn't empty, determine the highest value in the list and output the results to the console
    if len(marks) > 0:
        print("\nHighest Mark: %d" % max(marks))
        pause()

    else:
        print("\nList of marks is empty!")
        mini_pause()

def sort_marks():
    # If marks list isn't empty, show elements of the list in ascending order
    if len(marks) > 0:
        ascending_marks = marks.copy()
        ascending_marks.sort()

        print("\nMarks in ascending order: %s" % ascending_marks)
        pause()
    
    else:
        print("\nList of marks is empty!")
        mini_pause()

def splice():
    # If there are no global keyword, trying to modify marks will make it seem to the program that the scope is local and as such it will raise an error as there are no local marks list defined
    global marks

    # Will attempt to do the splicing only if the marks list isn't empty
    if len(marks) > 0:
        try:
            clear()
            
            tmp_list = [] # To temporarily store the sliced list
            
            display_marks()

            start_index = int(input("\nInput start of index to subset: "))
            end_index = int(input("Input end of index to subset: "))

            # Error checking conditions that prevents the index from going out of bounds
            if start_index < 0 or start_index > len(marks) or end_index < 0 or end_index > len(marks):
                print(
                    "\nStart/End index must not be lesser than 0 or greater than the length of the list of marks!")
                pause()

            # If start index > end index, there will be no data displayed 
            elif start_index > end_index:
                print("\nStart index must not be greater than end index!")
                pause()

            # If start index = end index, there will be no data displayed
            elif start_index == end_index:
                print("\nStart/End index must not be equal to each other!")
                pause()

            # If prior conditions has been satisfied, proceed to slice the list, data will be stored in a temporary list and will be copied back to the old list
            else:
                tmp_list = marks[start_index : end_index]
                marks = tmp_list.copy()
            
                print("\n%s" % marks)
                pause()

        except ValueError:
            print("\nInput must be numeric!")
            mini_pause()
    
    else:
        print("\nMarks list is empty!")
        mini_pause()

def remove_mark():
    # If marks list isn't empty, proceed to prompt user to enter index of elements to be removed
    if len(marks) > 0:
        clear()
        display_marks()
        
        try:
            remove_index = int(input("\nIndex to remove: "))
            
            # Error checking to prevent index from going out of bound
            if remove_index < 0 or remove_index >= len(marks):
                print("\nIndex must be between 0 to (length of marks -1)")
                pause()
            
            # Removes the element of a particular index and outputs the result to the console
            else:
                del(marks[remove_index])
                clear()
                display_marks()
                print("")
                pause()

        except ValueError:
            print("\nInput must be numeric!")
            mini_pause()
        
    else:
        print("\nMarks list is empty!")
        mini_pause()

def change_mark():
    # If marks list isn't empty, proceed to prompt user to enter the index of the element whose value needs to be changed
    if len(marks) > 0:
        clear()
        display_marks()

        try:
            change_index = int(input("\nIndex to change: "))

            # Error checking to prevent out of bounds issue
            if change_index < 0 or change_index >= len(marks):
                print("\nIndex must be between 0 to (length of marks -1)")
                pause()

            else:
                try:
                    new_value = int(input("Input new value: "))

                    # Error checking that only accepts values of 0-100
                    if new_value >=0 and new_value <= 100:
                        marks[change_index] = new_value
                        clear()
                        display_marks()
                        print("")
                        pause()
                    
                    else:
                        print("\nNew value must be in the range of 0-100!")
                        pause()

                except ValueError:
                    print("\nInput must be numeric!")
                    mini_pause()
                
        except ValueError:
            print("\nInput must be numeric!")
            mini_pause()

    else:
        print("\nMarks list is empty!")
        mini_pause()

def add_mark(): 
    clear()
    display_marks()

    try:
        new_mark = int(input("\nInput new mark: "))

        # Error checking that only allows accepts value of 0-100
        if new_mark >=0 and new_mark <= 100:
            marks.append(new_mark)
            clear()
            display_marks()
            print("")
            pause()
        
        else:
            print("\nNew value must be in the range of 0-100!")
            pause()

    except ValueError:
        print("\nInput must be numeric!")
        mini_pause()

def edit_list_menu():
    display_marks()
    print("\n1. Slice the list")
    print("2. Remove a mark from the list")
    print("3. Change a mark")
    print("4. Add new marks")
    print("5. Back to main menu")

    choice = input("\nPlease choose on how you want to edit the list: ")
    return(choice) 

def edit_list():
    # Only allows marks list to be edited as long as it is not an empty list
    if len(marks) > 0:
        while True:
            clear()
            choice = edit_list_menu()

            if choice == "1":
                splice()

            elif choice == "2":
                remove_mark()

            elif choice == "3":
                change_mark()

            elif choice == "4":
                add_mark()

            elif choice == "5":
                break   

            else:
                print("\nInvalid choice!")
                mini_pause()
    
    else:
        print("\nMarks list is empty!")
        mini_pause()

def entry():
    clear()

    # Loops until a -1 is entered
    while True:
        try:
            clear()
            count = len(marks) + 1 # For subsequent entries

            display_marks()

            mark_input = int(input("\nPlease enter marks for student %d or -1 to end: " % count))

            # If input entered is -1, exit while loop
            if mark_input == -1:
                break

            # Error checking that accepts only values of 0-100
            elif mark_input < 0 or mark_input > 100:
                print("\nMarks entered must be in the range of 0-100!")
                mini_pause()

            # If prior conditions are met, proceed to add new elements to the mark list
            else:
                marks.append(mark_input)

        except ValueError:
            print("\nThis is not a valid mark")
            mini_pause()

def menu():
    clear()

    print("+++ Welcome to the Marks Entry Simple System (MESS) +++")
    display_marks()

    print("\n1. Entry of marks to the MESS")
    print("2. Display the maximum mark in the MESS")
    print("3. Display the marks sorted in ascending order")
    print("4. Display a subset of marks in the MESS")

    choice = input("\nPlease choose 1-4 or press ENTER to quit: ")
    return(choice)

while True:
    choice = menu()

    if choice == "":
        print("\nGoodbye!")
        mini_pause()
        clear()
        break
    
    elif choice == "1":
        entry()

    elif choice == "2":
        max_marks()

    elif choice == "3":
        sort_marks()

    elif choice == "4":
        edit_list()
    
    else:
        print("\nInvalid choice!")
        mini_pause()


