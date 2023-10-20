import math


print("Weclome to BMI Calculator!")

weight = input("Please enter your current weight (KG): ")
height = input("Please enter your current height (Meters): ")

bmi = math.trunc((float(weight) / math.pow(float(height),2)))

if(bmi < 18.5):
    print("Your BMI is " + str(bmi) + ", you're in the underweight range.")
elif(bmi >= 18.5 and bmi <= 24.9):
    print("Your BMI is " + str(bmi) + ", you're in the healthy weight range.")
elif(bmi >= 25.0 and bmi <= 29.9):
    print("Your BMI is " + str(bmi) + ", you're in the overweight range.")
else:
    print("Your BMI is " + str(bmi) + ", you're in the obese range.")

