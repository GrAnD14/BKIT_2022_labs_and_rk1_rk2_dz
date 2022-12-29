from operator import itemgetter
class Teacher:
    def __init__(self, id, name, wage, id_course):
        self.id = id
        self.name = name
        self.wage = wage
        self.id_course = id_course
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
class Teacher_and_course:
    def __init__(self, id_teacher, id_course):
        self.id_teacher = id_teacher
        self.id_course = id_course
teachers = [
    Teacher(1, "Александров", 1000, 1),
    Teacher(2, "Иванов", 1500, 3),
    Teacher(3, "Барановский", 2000, 2),
    Teacher(4, "Егоров", 1600, 4),
    Teacher(5, "Ченский", 1800, 2),
    Teacher(6, "Соколов", 1300, 4),
    Teacher(7, "Сороковиков", 1900, 1),
    Teacher(8, "Смирнов", 1600, 3),
]
courses = [
    Course(1, "физика"),
    Course(2, "математика"),
    Course(3, "химия"),
    Course(4, "информатика")
    ]
teacherofcourse = [
    Teacher_and_course(1, 1),
    Teacher_and_course(2, 3),
    Teacher_and_course(3, 2),
    Teacher_and_course(4, 4),
    Teacher_and_course(5, 2),
    Teacher_and_course(6, 4),
    Teacher_and_course(7, 3),
    Teacher_and_course(8, 1),
    ]

def main():
    one_to_many =  [(t.name, t.wage, c.name)
            for t in teachers
            for c in courses
            if t.id_course == c.id]
    print('Task А1')
    res1 = sorted(one_to_many, key=itemgetter(2))
    print(res1)

    many_to_many_tmp = [(c.name, tc.id_course, tc.id_teacher)
                        for c in courses
                        for tc in teacherofcourse
                        if c.id == tc.id_course]
    many_to_many =  [(t.id, id_course)
            for name, id_course, id_teacher in many_to_many_tmp
            for t in teachers
            if t.id == id_teacher]
    print('Task А2')
    res2_unsorted = []
    for c in courses:
        c_courses = list(filter(lambda i:i[2]==c.name, one_to_many))
        if len(c_courses) > 0:
            c_sizes = [sal for _, sal, _ in c_courses]
            c_sizes_sum = sum(c_sizes) / 2
            res2_unsorted.append((c.name, c_sizes_sum))
    res2 = sorted(res2_unsorted, key=itemgetter(1), reverse=True)
    print(res2)

    many_to_many_temp = [(c.name, tc.id_course, tc.id_teacher)
                         for c in courses
                         for tc in teacherofcourse
                         if c.id == tc.id_course]
    many_to_many = [(t.name, t.wage, course_name)
            for course_name, id_course, id_teacher in many_to_many_temp
            for t in teachers
            if t.id == id_teacher]
    print('Task А3')
    res3 = {}
    for c in courses:
        if 'физика' in c.name:
            c_courses = list(filter(lambda i: i[2] == c.name, many_to_many))
            c_courses_names = [x for x, _, _ in c_courses]
            res3[c.name] = c_courses_names
    print(res3)

if __name__ == '__main__':
    main()

