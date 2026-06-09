num1 = float(input("შეიყვანე პირველი რიცხვი: "))
num2 = float(input("შეიყვანე მეორე რიცხვი: "))
operator = input("შეიყვანე ოპერატორი (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print("პასუხი:", result)
elif operator == "-":
    result = num1 - num2
    print("პასუხი:", result)
elif operator == "*":
    result = num1 * num2
    print("პასუხი:", result)
elif operator == "/":
    if num2 == 0:
        print("0-ზე გაყოფა არ შეიძლება")
    else:
        result = num1 / num2
        print("პასუხი:", result)
else:
    print("არასწორი ოპერატორი")
