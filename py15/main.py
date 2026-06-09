class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    def work(self):
        print("Employee is working")

    def raise_salary(self, amount):
        if amount < 0:
            raise ValueError("Raise amount cannot be negative")
        self.salary += amount


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def code(self):
        print("Writing code...")

    def work(self):
        print("Developer is coding")


class Designer(Employee):
    def __init__(self, name, salary, design_tool):
        super().__init__(name, salary)
        self.design_tool = design_tool

    def create_design(self):
        print("Creating design...")

    def work(self):
        print("Designer is designing")


developer = Developer("Nika", 3000, "Python")
designer = Designer("Mariam", 2500, "Figma")

developer.show_info()
developer.work()
developer.code()

designer.show_info()
designer.work()
designer.create_design()
