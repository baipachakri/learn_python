weight = float(input("enter your weight (in pounds): "))
height = float(input("enter your height : "))
bmi =  round(weight / (height**2))
bmi = 23
if bmi < 18.5:
    print(f"your bmi is {bmi} , you are underweight")
elif bmi < 25:
    print(f"your bmi is {bmi}, you have a normal weight")
elif bmi <30:
    print(f"your bmi is {bmi}, you are overweight")
elif bmi < 30 :
    print(f"your bmi is {bmi},you are obese")
else:
    print(f"your bmi is {bmi},you are clinically obese")
