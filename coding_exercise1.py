weight = int(input('Enter weight in kg: '))
height = float(input("Enter height in meter: "))

bmi = (weight/height**2)
print(bmi)
bmi = round(bmi)

print(bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi} and you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi} and your are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi} and you are obese.")
else:
    print(f"Your BMI is {bmi} and you are clinically obese")