class Student:
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def rate_lectur(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in lectur.courses_attached:
            if course in lectur.grades:
                lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Ошибка'

    def home_works_general(self):
        grades = self.grades.values()
        point = sum(sum(i) for i in grades)
        length = sum(len(i) for i in grades)
        exit_point = point / length
        return round(exit_point, 1)

    def __str__(self):
        delimiter = ', '
        speath = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.home_works_general()}\nКурсы в процессе изучения: {delimiter.join(self.courses_in_progress)}\nЗавершенные курсы: {delimiter.join(self.finished_courses)}'
        return speath

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    lectorur_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lectorur_list.append(self)

    def general_values(self):
        grades = self.grades.values()
        point = sum(sum(i) for i in grades)
        length = sum(len(i) for i in grades)
        exit_point = point / length
        return round(exit_point,1)

    def __str__(self):
        speath = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.general_values()}'
        return speath

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        speath = f'Имя: {self.name} \nФамилия: {self.surname}'
        return speath

class Number:
    def __init__(self, value):
        self.__value = value

    def __lt__(self, other):
        return self.__value < other.__value
#--------------------------------------------------------- ИНИЦИАЛИЗАЦИЯ ЭКЗЕМПЛЯРОВ КЛАССОВ
andrew_st = Student("Andrew", "Bulkin", "male")
marina_st = Student("Marina", "Stepanova", "female")
anna_le = Lecturer("Anna", "Bragina")
valery_le = Lecturer("Valery", "Zavinin")
gena_rw = Reviewer("Gennadiy", "Lonin")
olya_rw = Reviewer("Olya", "Suro")
#--------------------------------------------------------- ДОБАВЛЯЕМ ПРЕДМЕТЫ
andrew_st.courses_in_progress += ['Git', 'Python']
marina_st.courses_in_progress += ['Git', 'OOP']
andrew_st.finished_courses += ['OOP']
marina_st.finished_courses += ['Python']
anna_le.courses_attached += ['Git']
valery_le.courses_attached += ['Git', 'OOP']
gena_rw.courses_attached += ['Git']
olya_rw.courses_attached += ['Git', 'Python']
#--------------------------------------------------------- ВЫСТАВЛЯЕМ ОЦЕНКИ
andrew_st.rate_lectur(anna_le, "Git", 10)
andrew_st.rate_lectur(anna_le, "Git", 9)
andrew_st.rate_lectur(anna_le, "Git", 7)
marina_st.rate_lectur(valery_le, "Git", 10)
marina_st.rate_lectur(valery_le, "Git", 10)
marina_st.rate_lectur(valery_le, "Git", 10)
gena_rw.rate_hw(andrew_st, "Git", 9)
olya_rw.rate_hw(andrew_st, "Python", 4)
gena_rw.rate_hw(marina_st, "Git", 10)
gena_rw.rate_hw(marina_st, "OOP", 10)
#--------------------------------------------------------- ЗАДАНИЕ № 3
# print(gena_rw)
# print(anna_le)
# print(andrew_st)
#--------------------------------------------------------- СРАВНИВАЕМ ПО ОЦЕНКАМ
# test_1 = Number(andrew_st.home_works_general())
# test_2 = Number(marina_st.home_works_general())
# print(test_2 > test_1)

# print(Number(andrew_st.home_works_general()) > Number(marina_st.home_works_general()))

# print(Number(anna_le.general_values()) < Number(valery_le.general_values()))
#--------------------------------------------------------- ЗАДАНИЕ № 4 ДЛЯ СТУДЕНТОВ
def general_value_students(student_list, course_name):
    general = []
    for student in student_list:
        if course_name in student.grades:
            general.append(student.grades.get(course_name))

    point = sum(sum(i) for i in general)
    length = sum(len(i) for i in general)
    exit_point = point / length

    print(f'Средняя оценка по предмету {course_name} : {round(exit_point,1)}')

# test = general_value_students(Student.student_list, 'Git')
#--------------------------------------------------------- ЗАДАНИЕ № 4 ДЛЯ ЛЕКТОРОВ
def general_value_lecturer(lectorur_list, course_name):
    general = []
    for lectorer in lectorur_list:
        if course_name in lectorer.grades:
            general.append(lectorer.grades.get(course_name))

    point = sum(sum(i) for i in general)
    length = sum(len(i) for i in general)
    exit_point = point / length

    print(f'Средняя оценка по предмету {course_name} : {round(exit_point,1)}')

# test = general_value_lecturer(Lecturer.lectorur_list, 'Git')


