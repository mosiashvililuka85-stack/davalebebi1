import json
import random

from faker import Faker


fake = Faker()


students = []

for student_id in range(1, 101):
    students.append(
        {
            "student_id": student_id,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "age": random.randint(18, 70),
            "is_active": random.choice([True, False]),
        }
    )


with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)


with open("students.json", "r", encoding="utf-8") as file:
    loaded_students = json.load(file)


active_students = [
    student for student in loaded_students if student["is_active"] is True
]


with open("active_students.json", "w", encoding="utf-8") as file:
    json.dump(active_students, file, indent=4)

