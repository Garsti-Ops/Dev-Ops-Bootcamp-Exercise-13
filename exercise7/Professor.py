import Person


class Professor(Person.Person):
    subjects = []

    def __init__(self, last_name, first_name, age, subjects):
        super().__init__(first_name, last_name, age)
        self.subjects = subjects

    def list_subjects(self):
        print(self.subjects)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        self.subjects.remove(subject)