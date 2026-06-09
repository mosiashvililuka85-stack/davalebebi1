items = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
unique_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)

print("Original list:", items)
print("Unique list:", unique_items)
