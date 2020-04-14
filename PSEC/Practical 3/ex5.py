import os
import time

SLEEP_DURATION = 1.5    # Pause duration
port_dict = dict()      # Declares empty dictionary

def clear():
    os.system("cls")    # Clears current console

def pause():
    os.system("pause")  # Pause code execution until user press an input

def mini_pause():
    time.sleep(SLEEP_DURATION)  # The time for the program to sleep

def display_dict():
    print("These are the open ports found and their corresponding services:")

    # Iterates through every element in the dictionary and prints out the key and values to the console
    for element in port_dict:
        print(f"{element}:{port_dict[element]}")

def start():
    clear()

    # Removes whitespaces on input
    user_input = input("Please enter service:port that were found to be open, separated by '|'\n").strip()

    # Splits the whole string into individual pieces by using '|' as delimiter
    user_input = user_input.split('|')

    for individual_input in user_input:
        individual_input = individual_input.strip() # Removes whitespaces on input

        service, port = individual_input.split(':') # Splits the individual string into key and values by using ':' as delimeter

        port_dict[int(port)] = service.strip()  # Adds the abovementioned key, values into the dictionary
    
def search_openPort():
    if len(port_dict) > 0:  # If dictionary is empty, show an error message, else continue as per normal

        try:
            clear()
            port_input = int(input("Enter port: ").strip()) # Removes whitespaces from input

            # If the port to be searched is the dictionary, prints out the service to the console, else display an error message 
            if port_input in port_dict:
                print(f"\n{port_dict[port_input]} is running on port {port_input}")
                pause()

            else:
                print(f"\nNo service is running on port {port_input}") 
                pause()  

        except ValueError: # If user inputs a string instead of a number, an error message will be displayed
            print("\nPort must be numeric")
            mini_pause()
    
    else:
        print("\nDictionary is empty!")
        mini_pause()

def search_service():
    clear()

    if len(port_dict) > 0: # If dictionary is empty, show an error message, else continue as per normal

        service_input = input("Enter service: ").strip()

        not_found = True
        if service_input.isalpha(): # If user inputs numbers, an error message will be printed, else continue as per normal

            for port, service in port_dict.items(): # Iterates through every element in the dictionary and if service is found, flag not_found as false, display results in the console and breaks the for loop

                if service.lower() == service_input.lower():
                    not_found = False

                    print(f"\n{service} is running on port {port}")
                    pause()
                    break
            
            if not_found:
                print(f"\n{service} not found!")
                pause()
        
        else:
            print("\nPlease enter only string")
            mini_pause()

    else:
        print("\nDictionary is empty!")
        mini_pause()

def add_new_service_port():
    tmp_dict = dict() # Declares a new temp dictionary

    clear()

    # Removes whitespaces on input
    new_service_port = input(
        "Please enter service:port that were found to be open, separated by '|'\n").strip()

    # Splits the whole string into individual pieces by using '|' as delimiter
    new_service_port = new_service_port.split('|')

    for individual_service_port in new_service_port:
        individual_service_port = individual_service_port.strip()  # Removes whitespaces on input

        # Splits the individual string into key and values by using ':' as delimeter

        service, port = individual_service_port.split(':')
        # Adds the abovementioned key, values into the temp dictionary
        tmp_dict[int(port)] = service.strip()

    port_dict.update(tmp_dict)  # Updates the global dictionary with the new entries from the temp dictionary

    clear()
    display_dict()

    print("\nOpen ports and their corresponding services has been updated with the new input!")
    pause()

def remove_service():
    if len(port_dict) > 0: # If dictionary is empty, show an error message, else continue as per normal

        clear()
        service_to_be_removed = input("Enter service to be removed: ").strip()

        not_found = True
        if service_to_be_removed.isalpha():  # If user inputs numbers, an error message will be printed, else continue as per normal

            for port, service in port_dict.items():  # Iterates through every element in the dictionary and if service is found, flag not_found as false, deletes the particular service from dictionary and breaks the for loop

                if service.lower() == service_to_be_removed.lower():
                    not_found = False

                    print(f"\nRemoved {service} on port {port}")
                    del(port_dict[port])
                    pause()
                    break

            if not_found:
                print(f"\n{service_to_be_removed} not found!")
                pause()

        else:
            print("\nPlease enter only string")
            mini_pause()

    else:
        print("\nDictionary is empty!")
        mini_pause()

def change_port_number():
    if len(port_dict) > 0:  # If dictionary is empty, show an error message, else continue as per normal

        try:
            clear()
            # Removes whitespaces from input
            port_to_be_changed = int(input("Enter port to be changed: ").strip())

            # If the port to be changed is the dictionary, prints out the service to the console, else display an error message
            if port_to_be_changed in port_dict:
                new_port = int(input("Enter new port: ").strip())
              
                clear()
                display_dict()

                print(f"\nOld port {port_to_be_changed} updated to new port {new_port}")

                # https://stackoverflow.com/questions/16475384/rename-a-dictionary-key
                port_dict[new_port] = port_dict.pop(port_to_be_changed)

                pause()

            else:
                print(f"\nPort {port_to_be_changed} not found!")
                mini_pause()

        except ValueError:  # If user inputs a string instead of a number, an error message will be displayed
            print("\nPort must be numeric")
            mini_pause()

    else:
        print("\nDictionary is empty!")
        mini_pause()

def update_dict():
    while True:
        clear()
        display_dict()

        try:
            print("\n1) Add new service && port")
            print("2) Remove a service")
            print("3) Change port number")
            print("4) Back to main menu\n")

            choice = int(input("Please enter request: ").strip())

            if choice == 1:
                add_new_service_port()

            elif choice == 2:
                remove_service()

            elif choice == 3:
                change_port_number()

            elif choice == 4:
                break
        
        except ValueError:
            print("\nRequest must be numeric")
            mini_pause()

def menu():
    while True:
        clear()
        display_dict()

        try:
            print("\n1) Search for open port")
            print("2) Search for service running")
            print("3) Update dictionary")
            print("4) Exit\n")

            choice = int(input("Please enter request: ").strip())
        
            if choice == 1:
                search_openPort()

            elif choice == 2:
                search_service()

            elif choice == 3:
                update_dict()

            elif choice == 4:
                print("\nGoodbye!")
                mini_pause()
                clear()
                break

        except ValueError:
            print("\nRequest must be numeric")
            mini_pause()
        
start()
menu()

