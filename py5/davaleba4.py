long_names = []
short_names = []

while True:
    name = input("Enter name: ")
    name = name.strip()

    if name == "stop" or name == "Stop" or name == "exit" or name == "Exit" or name == "quit" or name == "Quit":
        break

    fixed_name = name.capitalize()

    if len(fixed_name) > 3:
        long_names.append(fixed_name)
    else:
        short_names.append(fixed_name)

print("Long names:", long_names)
print("Short names:", short_names)
