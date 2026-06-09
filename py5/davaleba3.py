import random


random_numbers = [random.randint(-50, 50) for i in range(20)]
even_numbers = [number for number in random_numbers if number % 2 == 0]

print("Random numbers:", random_numbers)
print("Even numbers:", even_numbers)
