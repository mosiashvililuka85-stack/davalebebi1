class Student:
    status = True
    pay = 1000

    def __init__(self, first_name, last_name, age, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_discount(self):
        if self.age < 18:
            self.pay = self.pay - (self.pay * 20 / 100)
        return self.pay

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    def get_status(self):
        average = self.calculate_average()

        if average > 90:
            return "Excellent"
        if average >= 70:
            return "Good"
        if average >= 50:
            return "Average"

        self.status = False
        return "Poor"
