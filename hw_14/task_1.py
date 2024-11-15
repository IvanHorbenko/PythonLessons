class TooManyStudentsError(Exception):
    def __init__(self, message="Not able to add more that 10 students"):
        self.message = message
        super().__init__(self.message)


class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student_name):
        if len(self.students) >= 10:
            raise TooManyStudentsError()
        self.students.append(student_name)
        print(f"{student_name} added to group {self.name}.")

try:
    group = Group("Programing on Python")

    for i in range(10):
        group.add_student(f"Student {i + 1}")

    group.add_student("Student 11")

except TooManyStudentsError as e:
    print(f"Error: {e}")
