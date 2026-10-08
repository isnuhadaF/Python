import unittest

from student import Student


class MyTestCase(unittest.TestCase):

    def test_that_student_name_is_set_correctly(self):
        student = Student('Dotun', "Dotman", 22)
        assert student.name == "Dotun"
        assert student.age == 22
        assert student.username == "Dotman"

    def test_that_student_address_is_set_correctly(self):
        student = Student('Dotun', "Dotman", 22)
        student.set_address(11516, "Ilu-peju")
        assert student.address == {"Zip" : 11516,
                                "City" : "Ilu-peju"}

    def test_that_student_record_can_be_retrieved(self):
        student = Student('Dotun', "Dotman", 22)
        student.set_address(11516, "Ilu-peju")
        assert student.get_record() == {"Name" : "Dotun",
                                        "Age" : 22,
                                        "City" : "Ilu-peju",
                                        "Address" : {"Zip" : 11516,
                                                     "City" : "Ilu-peju"}
                                        }
if __name__ == '__main__':
    unittest.main()
