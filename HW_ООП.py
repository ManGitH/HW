class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'''Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за домашнее задание: 
        \nКурсы в процессе изучения: {",".join(self.courses_in_progress)}\nзавершенные курсы: {",".join(self.finished_courses)}'''
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

    def avggrd(self):
        for l, g in self.grades.items():
            sum_ag = sum(g) / len(g)
        return sum_ag
    
    def __str__(self):
        res = f'''Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции: {print(self.avggrd)}'''
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


student_1 = Student('Sergey', 'Fetisov', 'm')
student_2 = Student('Andrey', 'Miroshnikov', 'm')
student_3 = Student('Aleksandr', 'Plotnikov', 'm')
best_student = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['PHP']
student_1.courses_in_progress += ['JS']
student_2.courses_in_progress += ['JS']
student_2.courses_in_progress += ['SQL']
student_3.courses_in_progress += ['SQL']
student_3.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['PHP']
student_1.finished_courses += ['Python']
student_1.finished_courses += ['SQL']
student_2.finished_courses += ['PHP']
student_2.finished_courses += ['Python']
student_3.finished_courses += ['JS']
student_3.finished_courses += ['PHO']
best_student.finished_courses += ['JS']
best_student.finished_courses += ['SQL']
sn = f'''Имена студентов: {student_1.name}, {student_2.name}, {student_3.name}, {best_student.name}'''
pc = f'''Курсы на которые записаны студенты: 
{student_1.name}-{student_1.courses_in_progress}, 
{student_2.name}-{student_2.courses_in_progress}, 
{student_3.name}-{student_3.courses_in_progress},
{best_student.name}-{best_student.courses_in_progress}'''
fc = f'''Курсы которые закончили студенты: 
                            {student_1.name}-{student_1.finished_courses}, 
                            {student_2.name}-{student_2.finished_courses}, 
                            {student_3.name}-{student_3.finished_courses},
                            {best_student.name}-{best_student.finished_courses}'''
print(sn)
print(pc)
print(fc)

mentor_1 = Mentor('Oleg', 'Sherbakov')
mentor_2 = Mentor('Andrey', 'Martynenko')
mentor_3 = Mentor('Uri', 'Sinatulin')
cool_mentor = Mentor('Some', 'Buddy')
# mentor_1.courses_attached += ['PHP']
# mentor_2.courses_attached += ['JS']
# mentor_3.courses_attached += ['SQL']
# cool_mentor.courses_attached += ['Python']
mn = f'''Имена менторов: {mentor_1.name}, {mentor_2.name}, {mentor_3.name}, {cool_mentor.name}'''
print(mn)

lecturer_1 = Lecturer('Aleksandr', 'Knips')
lecturer_2 = Lecturer('Slava', 'Nazarevich')
lecturer_1.courses_attached += ['PHP']
lecturer_1.courses_attached += ['SQL']
lecturer_2.courses_attached += ['JS']
lecturer_2.courses_attached += ['Python']
student_1.rate_lecturer = (lecturer_1, 'PHP', 10)
student_2.rate_lecturer = (lecturer_1, 'PHP', 6)
student_3.rate_lecturer = (lecturer_2, 'JS', 9)
best_student.rate_lecturer = (lecturer_2, 'JS', 5)
ln = f'''Имена лекторов: {lecturer_1}, {lecturer_2}'''
lc = f'''Курсы которые ведут лекторы: 
                            {lecturer_1.name}-{lecturer_1.courses_attached}, 
                            {lecturer_2.name}-{lecturer_2.courses_attached}'''
# lg = f'''Оценки студентов лекторам: {lecturer_1.name}-{}, {lecturer_2.name}'''

# print(ln)
# print(lc)
print(lecturer_1)

reviewer_1 = Reviewer('Artem', 'Bibanin')
reviewer_2 = Reviewer('Some', 'Buddy')
reviewer_1.rate_hw(student_1, 'PHP', 8)
reviewer_2.rate_hw(student_2, 'JS', 6)
print(reviewer_1.name, reviewer_2.name)

print(student_1)


# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)