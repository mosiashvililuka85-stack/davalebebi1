fruits = {}

while True:
    fruit = input("Enter your favorite fruit: ")

    if fruit == "stop":
        break

    if fruit in fruits:
        fruits[fruit] = fruits[fruit] + 1
    else:
        fruits[fruit] = 1

print(fruits)
