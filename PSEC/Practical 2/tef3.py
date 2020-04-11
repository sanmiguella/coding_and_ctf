try:
    years_in_service = int( input("Enter number of years in service: ") )
    current_salary = int( input("Enter current salary: ") )

    if (years_in_service < 10):
        
        if (current_salary < 1000):
            print("\nYour increment is $100")
        elif (current_salary < 2000):
            print("\nYour increment is $200")
        else: # Salary is $2000 or greater
            print("\nYour increment is $300")

    else:     # years in service is 10 or more

        if (current_salary < 1000):
            print("\nYour increment is $200")
        elif (current_salary < 2000):
            print("\nYour increment is $300")
        else: # Salary is $2000 or greater
            print("\nYour increment is $400")
    
except ValueError:
    print("\nInput entered wasn't a number!")
