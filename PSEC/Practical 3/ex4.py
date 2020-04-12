import os
import time

marks = []

def clear():
    os.system("cls")

def pause():
    os.system("pause")

def mini_pause():
    time.sleep(1)

def display_marks():
    if (len(marks) > 0):
            print("Current marks for %d students stored in system." % len(marks))
            print(marks)

def max_marks():
    if len(marks) > 0:
        print("\nHighest Mark: %d" % max(marks))
        pause()

    else:
        print("\nList of marks is empty!")
        mini_pause()

def sort_marks():
    if len(marks) > 0:
        ascending_marks = marks.copy()
        ascending_marks.sort()
        print("\nMarks in ascending order: %s" % ascending_marks)
        pause()
    
    else:
        print("\nList of marks is empty!")
        mini_pause()

def splice():
    global marks

    if len(marks) > 0:
        try:
            clear()
            
            tmp_list = []
            
            display_marks()

            start_index = int(input("\nInput start of index to subset: "))
            end_index = int(input("Input end of index to subset: "))

            if start_index < 0 or start_index > len(marks) or end_index < 0 or end_index > len(marks):
                print(
                    "\nStart/End index must not be lesser than 0 or greater than the length of the list of marks!")
                pause()

            elif start_index > end_index:
                print("\nStart index must not be greater than end index!")
                pause()

            elif start_index == end_index:
                print("\nStart/End index must not be equal to each other!")
                pause()

            else:
                tmp_list = marks[start_index: end_index]
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
    if len(marks) > 0:
        clear()
        display_marks()
        
        try:
            remove_index = int(input("\nIndex to remove: "))
            
            if remove_index < 0 or remove_index >= len(marks):
                print("\nIndex must be between 0 to (length of marks -1)")
                pause()
            
            else:
                del(marks[remove_index])
                clear()
                display_marks()
                pause()

        except ValueError:
            print("\nInput must be numeric!")
            mini_pause()
        
    else:
        print("\nMarks list is empty!")
        mini_pause()

def change_mark():
    global marks

    if len(marks) > 0:
        clear()
        display_marks()

        try:
            change_index = int(input("\nIndex to change: "))

            if change_index < 0 or change_index >= len(marks):
                print("\nIndex must be between 0 to (length of marks -1)")
                pause()

            else:
                try:
                    new_value = int(input("Input new value: "))

                    if new_value >=0 and new_value <= 100:
                        marks[change_index] = new_value
                        clear()
                        display_marks()
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
    global marks
    
    clear()
    display_marks()

    try:
        new_mark = int(input("\nInput new mark: "))

        if new_mark >=0 and new_mark <= 100:
            marks.append(new_mark)
            clear()
            display_marks()
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

    while True:
        try:
            clear()
            count = len(marks) + 1

            display_marks()

            mark_input = int(input("\nPlease enter marks for student %d or -1 to end: " % count))

            if mark_input == -1:
                break

            elif mark_input < 0:
                print("\nNegative values other than -1 is not valid.")
                mini_pause()

            elif mark_input > 100:
                print("\nValid marks are between 0 to 100.")
                mini_pause()

            else:
                marks.append(mark_input)
                count += 1

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


