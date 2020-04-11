open_ports = input("Please enter ports that were found to be open separated by | : ")

# Strips off spaces so searching wouldn't be a problem later
search_port = input("\nPlease input port number for your 'service': ").strip()

# '|' is used as a delimiter, so different ports are split by '|'
open_ports = open_ports.split('|')

list_of_ports = [] # Declares empty list

# Iterates through every port in the list and if there are whitespaces, remove it and add it to the list -> list_of_ports[]
for port in open_ports:
    list_of_ports.append(port.strip())

port_found = False
for port in list_of_ports:
    if search_port == port:
        port_found = True
        break # If port is found, exit for loop

if (port_found): # port_found == True
    print("\nYes, port %s is open!" % search_port)
else:            # port_found == False
    print("\nSorry, port %s is closed!" % search_port)
    print("Please choose from %s" % list_of_ports)
