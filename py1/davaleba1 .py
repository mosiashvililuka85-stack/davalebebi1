import math

a = int(input("შეიყვანეთ პირველი კათეტის სიგრძე: "))
b = int(input("შეიყვანეთ მეორე კათეტის სიგრძე: "))

c = math.sqrt(a * a + b * b)
s = a * b / 2

print("ჰიპოთენუზის სიგრძეა:", c)
print("ფართობია:", s)
