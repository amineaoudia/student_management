import csv
import math
from student import Student


class GradeManager:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load_data(self):
        self.students.clear()
        with open(self.filename, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # ignorer l'en-tête
            for row in reader:
                name = row[0]
                grade = float(row[1])
                self.students.append(Student(name, grade))

    def average_grade(self):
        return sum(s.grade for s in self.students) / len(self.students)

    def median_grade(self):
        grades = sorted(s.grade for s in self.students)
        n = len(grades)
        mid = n // 2
        if n % 2 == 0:
            return (grades[mid - 1] + grades[mid]) / 2
        return grades[mid]

    def standard_deviation(self):
        mean = self.average_grade()
        variance = sum((s.grade - mean) ** 2 for s in self.students) / len(self.students)
        return math.sqrt(variance)

    def best_student(self):
        return max(self.students, key=lambda s: s.grade)

    def worst_student(self):
        return min(self.students, key=lambda s: s.grade)

    def admitted_students(self):
        return [s for s in self.students if s.grade >= 10]

    def failed_students(self):
        return [s for s in self.students if s.grade < 10]
