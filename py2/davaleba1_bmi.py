weight = float(input("შეიყვანე წონა კილოგრამებში: "))
height = float(input("შეიყვანე სიმაღლე მეტრებში: "))

bmi = weight / (height ** 2)

print("შენი BMI არის:", bmi)

if bmi < 19:
    print("შენ ხარ underweight")
elif bmi <= 25:
    print("შენ ხარ normalweight")
else:
    print("შენ ხარ overweight")
