import csv
from random import randint

from faker import Faker


fake = Faker()

fieldnames = ["ID", "first_name", "last_name", "age"]

with open("persons.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for person_id in range(1, 51):
        writer.writerow(
            {
                "ID": person_id,
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "age": randint(20, 80),
            }
        )
