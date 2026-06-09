my_list = [(1, 3), (4, 2), (2, 5)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)


def divide_numbers():
    try:
        num1 = int(input("შეიყვანე პირველი რიცხვი: "))
        num2 = int(input("შეიყვანე მეორე რიცხვი: "))
        result = num1 / num2
        return result
    except ValueError:
        print("გთხოვ შეიყვანე მხოლოდ მთელი რიცხვები.")
    except ZeroDivisionError:
        print("ნულზე გაყოფა არ შეიძლება.")


print(divide_numbers())


from functools import reduce

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]

cheap_products = list(filter(lambda product: product["price"] < 100, products))
print(cheap_products)

all_products = list(map(lambda product: f'{product["name"]} - {product["price"]}', products))
print(all_products)

sorted_products = sorted(products, key=lambda product: product["price"])
print(sorted_products)

total_price = reduce(lambda total, product: total + product["price"], products, 0)
print(total_price)


def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n - 1)


print(sum_numbers(5))
