marks = [80, 39, 79, 81, 79, 70, 44, 57, 76, 46, 86, 29]

print("\nThe 10 students scored %s." % marks)
print("\nScores that qualify for 'A' grade are:")

# Only prints marks that are greater or equal to 80
for individual_mark in marks:
    if individual_mark >= 80:
        print(individual_mark)

# Copies existing list into a new list and sort them in ascending order
ascending_marks = marks.copy()
ascending_marks.sort()

print("\na) Marks in ascending order: %s" % ascending_marks)

# Copies existing list into a new list and sort them in descending order
descending_marks = marks.copy()     
descending_marks.sort(reverse=True)

print("b) Marks in descending order: %s" % descending_marks)

max_mark = max(marks)   # Getting the maximum value in the list
min_mark = min(marks)   # Getting the minimum value in the list

print("c) Highest Mark: %d" % max_mark)
print("d) Lowest Mark: %d" % min_mark)

# For every mark in the list marks, if there are any mark which are lower than 50, append them to the list of failed marks
failed_marks = [] 
for individual_mark in marks:
    if individual_mark < 50:
        failed_marks.append(individual_mark)

# Prints out the indexes of students who failed
output = ""
for individual_fail_mark in failed_marks:
    output += " " + str(marks.index(individual_fail_mark)) 

output = output.strip() # Removes whitespaces
print("e) Index(es) of students who failed: %s\n" % output)
