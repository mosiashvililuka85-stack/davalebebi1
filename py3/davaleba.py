print("1) ფაქტორიალი")
number = int(input("შეიყვანე რიცხვი: "))

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("ფაქტორიალია:", factorial)


print("\n2) გამრავლების ტაბულა")

for i in range(1, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i * j)


print("\n3) გადახდის აპარატი")

price = 50
paid = 0

print("გადასახდელი თანხაა:", price, "ლარი")

while paid < price:
    bill = int(input("შეიტანე კუპიურა (5, 10 ან 20): "))

    if bill == 5 or bill == 10 or bill == 20:
        paid = paid + bill
        remaining = price - paid

        if remaining > 0:
            print("დარჩენილია გადასახდელი:", remaining, "ლარი")
    else:
        print("შეიტანე ვალიდური კუპიურა")

change = paid - price
print("ხურდა:", change, "ლარი")
