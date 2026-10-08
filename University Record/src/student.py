

class Student:
    def __init__(self, name, username, age):
        self.name = name
        self.username = username
        self.age = age
        self.address = {}
        self.courses = []
        self.record = {}


    def set_name(self, name):
        self.record["Name"] = name

    def set_age(self, age):
        self.record["Age"] = age

    def add_courses(self, courses: list):
        self.courses = courses

    def set_address(self, zipcode, city):
        self.address["Zip"] = zipcode
        self.address["City"] = city
        self.record["Addresses"] = self.address

    def get_record(self):
        return self.record

    def get_username(self):
        return self.username

class Something:
    def __init__(self):
        pass

