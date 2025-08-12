# BMI-Calculator
Weight=float(input("Enter the Weight in kg= "))
Height=float(input("Enter the height in m = "))
BMI=Weight/(Height*Height)

print(f"\nYour BMI is: {BMI}")

#Responses according to conditions 
if BMI<18.5:
  print("You are underweight")
elif (BMI>=18.5, BMI<24.9):
  print("You have a normal weight")
elif BMI>24.9:
  print("You are overweight ")
else:
  print("You are obese")
  
