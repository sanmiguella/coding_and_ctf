restaurant_dishes = input("Please enter your restaurant dishes, separated by comma ',' : ")

# Removes whitespaces from food to be searched
food_to_search = input("\nPlease input food to search : ").strip()

# ',' is used as a delimeter, so different dishes are split by ','
restaurant_dishes = restaurant_dishes.split(',')

list_of_dishes = [] # Declares an empty list

# Iterates through every food in the restaurant dishes and if there are whitespaces, remove it and add it to the list -> list_of_dishes[]
for food in restaurant_dishes:
    list_of_dishes.append(food.strip())

similar_dishes = [] # Declares an empty list

for food in list_of_dishes:
    # On every iteration, compares both the item in the list as well as the food to be search in lowercase form, in short, searching is done with no regards to casing
    tmp = food.lower()

    # If the `food to be search` string exist inside a `food` string
    if tmp.find(food_to_search.lower()) != -1:
       similar_dishes.append(food)

# There are dishes similar to the search keyword
if len(similar_dishes) > 0: 
    print("\nYes , we serve the following:")

    for dish in similar_dishes:
        print(dish)

# No dishes similar to the search keyword
else:
    print("\nSorry, we don't serve %s!" % food_to_search)
    print("\nPlease choose from:\n%s" % list_of_dishes)