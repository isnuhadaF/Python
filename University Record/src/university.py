

class University:
    def __init__(self, students):
        self.name = "Shine Shine Institute"
        self.students = {}

    def add_student(self, name, student):
        self.students[name] = student

    def get_student(self, name):
        return self.students[name]
