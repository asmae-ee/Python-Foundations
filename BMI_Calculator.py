def bmi_calculator(weight, height):
     bmi = weight / (height * height)
     return bmi

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = bmi_calculator(weight, height)
print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi <= 25:
    print("You are normal")
elif 25 <= bmi <= 30:
    print("You are overweight")
elif bmi > 30:
    print("You are obese")
