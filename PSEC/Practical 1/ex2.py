# Weight and height is converted to type float upon input
weight = float( input("Enter your weight : ") )
height = float( input("Enter your height : ") )

bmi = weight / (height**2)
print("Your BMI is [ %.1f ]" % bmi)