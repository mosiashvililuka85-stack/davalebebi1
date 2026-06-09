seconds = int(input("შეიყვანეთ წამების რაოდენობა: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print("საათები:", hours)
print("წუთები:", minutes)
print("წამები:", remaining_seconds)
