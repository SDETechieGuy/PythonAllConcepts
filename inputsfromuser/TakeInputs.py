''' Multi-Line comment
college=input("What is your College Name:? ")
print("Your college name is: ",college)

name = input("What is your name:? ")
color = input("What is your favorite color:? ")
print(name," likes ",color)

'''

'''
#Type Conversion- to calculate age from inputting date of birth
birth_year = input("Pls enter your birth year: ")
current_year = 2025
#age = current_year - birth_year #TypeError: unsupported operand types
age = current_year - int(birth_year)
print("Yours age is: ",age) #44
'''

#Convert weight in pounds into kg
weight_pounds = input("Enter your weight in pounds: ")
print("Your weight in pounds is: ",weight_pounds)
weight_kg = int(weight_pounds) * 2.20462
print("Your weight in kgs is: ",weight_kg)