class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: ({self.name}, {self.age})"


def serialize_person(person):
    return f"Name: {person.name}, Age: {person.age}"


def deserialize_person(data):
    parts = data.strip().split(", ")

    name = parts[0].split(": ")[1]
    age = int(parts[1].split(": ")[1])

    return Person(name, age)


p1 = Person("Otar", 34)

serialized_data = serialize_person(p1)

with open("person.txt", "w") as file:
    file.write(serialized_data)

with open("person.txt", "r") as file:
    data_from_file = file.readline()

p2 = deserialize_person(data_from_file)

print(data_from_file)
print(p2)
