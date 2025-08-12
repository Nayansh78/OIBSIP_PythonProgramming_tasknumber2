# BMI-Calculator
Weight = float(input("Enter the Weight in kg = "))
Height = float(input("Enter the height in m = "))
BMI = Weight / (Height * Height)

print(f"\nYour BMI is: {BMI:.2f}")  # Rounded to 2 decimal places

# Responses according to conditions
if BMI < 18.5:
    print("You are underweight")
elif BMI >= 18.5 and BMI < 24.9:
    print("You have a normal weight")
elif BMI >= 25 and BMI < 29.9:
    print("You are overweight")
else:
    print("You are obese")
