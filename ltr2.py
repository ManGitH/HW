# class Person:
#     def __init__(self, id):
#         self.id = id
# some_person = Person(100)
# some_person.__dict__['age'] = 30
# print(some_person.age + len(some_person.__dict__))

# class Income:
#     def __init__(self, id_):
#         self.id_ = id_
#         id_ = 100
# income_1 = Income(1000)
# print(income_1. id_)

# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finishing_courses = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lectures, course, grade):
        if isinstance(lectures, Lectures) and course in lectures.courses_attached and course in self.courses_in_progress:
            if course in lectures.grades:
                lectures.grades[course] += [grade]
            else:
                lectures.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lectures(Mentor, Student):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # def avg_grade(self, grades):
    #     for l,g in grades.items:
    #         for i in g:
    #             sum_ag = sum(g)/len(g)
    #             return sum_ag

    def __str__(self, grades):
        for l,g in grades.items:
            for i in g:
                sum_ag = sum(g)/len(g)
                # return sum_ag
                res = f'''Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции:{sum_ag}'''
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'''Имя:{self.name}\nФамилия:{self.surname}'''
        return res

some_student1 = Student('Some', 'Student1', 'mail')
some_student2 = Student('Some', 'Student2', 'femail')
some_student1.finished_courses += ['Phyton']
some_student2.finished_courses += ['php']
some_student1.courses_in_progress += ['php']
some_student2.courses_in_progress += ['Phyton']
some_student1.add_courses('JS')
# some_student2.rate_lecture()
print(some_student1.finished_courses)
print(some_student1.courses_in_progress)


some_mentor1 = Mentor('Some', 'Mentor1')
some_mentor2 = Mentor('Some', 'Mentor2')
some_mentor1.courses_attached += ['Phyton']
some_mentor2.courses_attached += ['php']
#
some_lectore1 = Lectures('Some', 'Mentor1')
some_lectore2 = Lectures('Some', 'Mentor2')
some_lectore1.courses_attached += ['php']
some_lectore2.courses_attached += ['Phyton']
some_student2.rate_lecture(some_lectore1, 'Phytone', 8)
print(some_lectore1.grades)

some_reviewer1 = Reviewer('Some', 'Mentor1')
some_mentor2 = Reviewer('Some', 'Mentor2')
some_reviewer1.rate_hw(some_student1, 'Phyton', 9)

print(some_lectore1)

#
# # some_buddy = Mentor(Some, Boddy, php)
# # some_lecture = Lectures('Some', 'Lecture')
# # print(some_lecture)
#
# some_reviewer = Reviewer('Some', 'Reviewer')
# print(some_reviewer)

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# # best_student_2 = Student('Andrey', 'Martynenko', 'mail')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# # cool_mentor_2 = Mentor('Oleg', 'Bulgin')
# cool_mentor.courses_attached += ['Python']
#
# best_student.rate_lectures(cool_mentor, 'Python', 10)
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)


# print(best_student.rate_lectures(cool_mentor, 'Python', 10))