numbers = [10, 20, 30, 40, 50]

total = 0
count = 0

for number in numbers:
    total = total + number
    count = count + 1

average = total / count

print("List:", numbers)
print("Sum:", total)
print("Average:", average)
