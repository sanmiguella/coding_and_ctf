years_in_service = input("Enter number of years in service: ")

if (years_in_service.isdigit()):        
    years_in_service = int(years_in_service)

    current_salary = input("Enter current salary: ")

    if (current_salary.isdigit()):      
        current_salary = int(current_salary)

        if (years_in_service < 10):
            
            if (current_salary < 1000):
                print("\nYour increment is $100")
            
            elif (current_salary < 2000):
                print("\nYour increment is $200")

            else:   # Current salary is $2000 or greater
                print("\nYour increment is $300")

        else:       # years_in_service is 10 or greater
            if (current_salary < 1000):
                print("\nYour increment is $200")

            elif (current_salary < 2000):
                print("\nYour increment is $300")

            else:   # Current salary is $2000 or greater
                print("\nYour increment is $400")

    else:
        print("\nSalary should be numeric.")

else:
    print("\nNumber of years should be numeric.")
