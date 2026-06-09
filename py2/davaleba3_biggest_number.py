num1 = float(input("შეიყვანე პირველი რიცხვი: "))
num2 = float(input("შეიყვანე მეორე რიცხვი: "))
num3 = float(input("შეიყვანე მესამე რიცხვი: "))

if num1 == num2 or num1 == num3 or num2 == num3:
    print("გთხოვ შეიყვანო განსხვავებული რიცხვები")
else:
    if num1 > num2 and num1 > num3:
        print("ყველაზე დიდი რიცხვია:", num1)
    elif num2 > num1 and num2 > num3:
        print("ყველაზე დიდი რიცხვია:", num2)
    else:
        print("ყველაზე დიდი რიცხვია:", num3)
