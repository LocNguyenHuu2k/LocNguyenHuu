height_cm = int(input("Height = (cm)"))

weight = int(input("Weight = (kg)"))

height_m =  height_cm/100


BMI = weight / (height_m**2)

print(" Your BMI(Body Mass Idex) is",BMI )

if BMI < 16:
    print("Severely Underweight")
elif BMI <= 18.5:
    print(" Underweight")
elif BMI <= 25:
    print("Normal")
elif BMI <= 30:
    print("Overweight")
else :
    print("Obese")
