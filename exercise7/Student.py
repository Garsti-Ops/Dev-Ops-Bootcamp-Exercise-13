import Person


class Student(Person.Person):
    lectures = []

    def __init__(self, last_name, first_name, age, lectures):
        super().__init__(first_name, last_name, age)
        self.lectures = lectures

    def list_lectures(self):
        print(self.lectures)

    def add_lecture(self, lecture):
        self.lectures.append(lecture)

    def leave_lecture(self, lecture):
        self.lectures.remove(lecture)
