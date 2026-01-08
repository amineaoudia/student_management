class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name} : {self.grade}"
