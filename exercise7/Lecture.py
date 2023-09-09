class Lecture:
    name = ""
    max_number_of_students = 0
    duration = 0
    professors = []

    def __init__(self, name, max_number_of_students, duration, professors):
        self.name = name
        self.max_number_of_students = max_number_of_students
        self.duration = duration
        self.professors = professors

    def print_name(self):
        print(self.name)

    def add_professor(self, prof):
        self.professors.append(prof)