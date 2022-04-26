def avg_grd(a, b):
    avg = {}
    for l, g in b.items():
        sum_ag = sum(g) / len(g)
        avg[l] = sum_ag
    res = f'''{avg}'''
    return res


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'''Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за домашнее задание: {avg_grd(self, self.grades)}
        \nКурсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}'''
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        res = f'''Имя:{self.name}\nФамилия:{self.surname}'''
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'''Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции: {avg_grd(self, self.grades)}'''
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


student1 = Student('Andrey', 'Martynenko', 'm')
student1.courses_in_progress = ['Python', 'GIT']
student1.finished_courses = ['PHP', 'SQL']

student2 = Student('Dasha', 'Yacenko', 'f')
student2.courses_in_progress = ['PHP', 'SQL']
student2.finished_courses = ['Python', 'GIT']


mentor1 = Mentor('Oleg', 'Sherbakov')
mentor1.courses_attached = ['Python', 'GIT', 'PHP', 'SQL']
mentor2 = Mentor('Sergei', 'Fetisov')
mentor2.courses_attached = ['Python', 'GIT', 'PHP', 'SQL']
print(mentor1)
print(mentor2)

lector1 = Lecturer('Oleg', 'Sherbakov')
lector1.courses_attached = ['Python', 'GIT', 'PHP', 'SQL']
student1.rate_lecturer(lector1, 'PHP', 5)
student1.rate_lecturer(lector1, 'GIT', 5)
student1.rate_lecturer(lector1, 'Python', 5)
student1.rate_lecturer(lector1, 'SQL', 5)
student2.rate_lecturer(lector1, 'PHP', 9)
student2.rate_lecturer(lector1, 'GIT', 8)
student2.rate_lecturer(lector1, 'Python', 2)
student2.rate_lecturer(lector1, 'SQL', 1)
print(lector1)

reviewer1 = Reviewer('Sergei', 'Fetisov')
reviewer1.courses_attached = ['Python', 'GIT', 'PHP', 'SQL']
reviewer1.rate_hw(student1,'PHP', 5)
reviewer1.rate_hw(student1, 'GIT', 5)
reviewer1.rate_hw(student1,'Python', 5)
reviewer1.rate_hw(student1,'PSQL', 5)
reviewer1.rate_hw(student2,'PHP', 4)
reviewer1.rate_hw(student2, 'GIT', 3)
reviewer1.rate_hw(student2,'Python', 2)
reviewer1.rate_hw(student2,'PSQL', 1)
print(reviewer1)
print(student1)
print(student2)