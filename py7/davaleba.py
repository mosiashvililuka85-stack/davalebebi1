persons = [
    ("Kelly", "Simpson", 26),
    ("Erika", "Stephens", 24),
    ("Cheryl", "Dunn", 30),
    ("Amy", "Larsen", 49),
    ("Christine", "Gordon", 23),
    ("Monica", "Huff", 38),
    ("David", "Nixon", 36),
    ("Cindy", "Escobar", 41),
    ("Cindy", "White", 33),
    ("Joel", "Hall", 43),
    ("Steven", "Winters", 28),
    ("Alex", "Cole", 68),
    ("Alex", "Smith", 32),
    ("Brittany", "Thompson", 18),
    ("Ernest", "Young", 43),
    ("Traci", "Wells", 38),
    ("Andrew", "Flores", 61),
    ("Christopher", "Lewis", 29),
    ("Kevin", "Willis", 57),
    ("Kayla", "Lucas", 28),
    ("Michelle", "Rush", 43),
    ("Thomas", "Mason", 37),
]


def task_1():
    print("ამოცანა 1")

    while True:
        first_name = input('შეიყვანეთ სახელი (ან "stop"): ')
        if first_name == "stop":
            break

        matching_by_name = [person for person in persons if person[0] == first_name]
        if not matching_by_name:
            print("მოცემული სახელი არ არსებობს სიაში.")
            continue

        last_name = input('შეიყვანეთ გვარი (ან "stop"): ')
        if last_name == "stop":
            break

        matching_person = None
        for person in matching_by_name:
            if person[1] == last_name:
                matching_person = person
                break

        if matching_person is None:
            print("მოცემული გვარი არ არსებობს სიაში.")
            continue

        print(f"{matching_person[0]} {matching_person[1]} - ასაკი: {matching_person[2]}")


def task_2():
    print("\nამოცანა 2")

    word1 = input("შეიყვანეთ პირველი სიტყვა: ")
    word2 = input("შეიყვანეთ მეორე სიტყვა: ")

    set1 = set(word1)
    set2 = set(word2)

    common_chars = set1 & set2
    different_chars = set1 ^ set2
    union_chars = set1 | set2

    print("საერთო სიმბოლოები:", common_chars)
    print("განსხვავებული სიმბოლოები:", different_chars)
    print("გაერთიანებული სიმბოლოები:", union_chars)


task_1()
task_2()
