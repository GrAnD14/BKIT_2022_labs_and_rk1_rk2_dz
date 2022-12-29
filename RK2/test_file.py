import unittest
from changed_rk1 import *

class rk_test(unittest.TestCase):
    def setUp(self):
        self.courses = [
            Course(1, "физика"),
            Course(2, "математика"),
            Course(3, "химия"),
            Course(4, "информатика")
        ]
        self.teachers = [
            Teacher(1, "Александров", 1000, 1),
            Teacher(2, "Иванов", 1500, 3),
            Teacher(3, "Барановский", 2000, 2),
            Teacher(4, "Егоров", 1600, 4),
            Teacher(5, "Ченский", 1800, 2),
            Teacher(6, "Соколов", 1300, 4),
            Teacher(7, "Сороковиков", 1900, 1),
            Teacher(8, "Смирнов", 1600, 3),
        ]
        self.teachers_and_courses = [
            Teacher_and_course(1, 1),
            Teacher_and_course(2, 3),
            Teacher_and_course(3, 2),
            Teacher_and_course(4, 4),
            Teacher_and_course(5, 2),
            Teacher_and_course(6, 4),
            Teacher_and_course(7, 3),
            Teacher_and_course(8, 1),
        ]
    def test_A1(self):
        expected_result = [
        ('Егоров', 1600, 'информатика'),
        ('Соколов', 1300, 'информатика'),
        ('Барановский', 2000, 'математика'),
        ('Ченский', 1800, 'математика'),
        ('Александров', 1000, 'физика'),
        ('Сороковиков', 1900, 'физика'),
        ('Иванов', 1500, 'химия'),
        ('Смирнов', 1600, 'химия'),
        ]
        result = A1(self.courses, self.teachers)
        self.assertEqual(result, expected_result)
    def test_A2(self):
        expected_result = [
            ('математика', 1900.0),
            ('химия', 1550.0),
            ('физика', 1450.0),
            ('информатика', 1450.0)
        ]
        result = A2(self.courses, self.teachers)
        self.assertEqual(result, expected_result)
    def test_A3(self):
        expected_result = {
            'физика': ['Александров', 'Смирнов'],
        }
        result = A3(self.courses, self.teachers)
        self.assertEqual(result, expected_result)
if __name__ == '__main__':
    unittest.main()
