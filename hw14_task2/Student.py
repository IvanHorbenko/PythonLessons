class Student:
    def __init__(self, gender, age, first_name, last_name, group_id):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.group_id = group_id

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        return hash(str(self))
