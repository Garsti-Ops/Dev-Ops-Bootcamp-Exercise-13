from datetime import datetime


class Employee:
    name = ""
    years_of_experience = 0
    job_title = ""
    date_of_birth = datetime.now()

    def __init__(self, name, years_of_experience, job_title, date_of_birth):
        self.name = name
        self.years_of_experience = years_of_experience
        self.job_title = job_title
        self.date_of_birth = date_of_birth

    def get_values_as_array(self):
        return [self.name, self.years_of_experience, self.job_title, datetime.strftime(self.date_of_birth,"%y-%m-%d")]
