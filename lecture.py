class Lecture:
    def __init__(self, name, max_students, duration, professors):
        self.name = name
        self.max_student = max_students
        self.duration_minuts = duration
        self.professors = professors

    def print_name_and_duration(self):
        print(f"{self.name} - {self.duration_minuts} minutes")

    def add_professors(self, new_professor):
        self.professors.append(new_professor)
