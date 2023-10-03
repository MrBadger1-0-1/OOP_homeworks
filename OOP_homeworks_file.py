class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectur(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in lectur.courses_attached:
            if course in lectur.grades:
                lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

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

andrew = Student("Andrew", "Bulkin", "male")
anna = Lecturer("Anna", "Bragina")
gena = Reviewer("Gennadiy", "Lonin")

andrew.courses_in_progress += ['Git']
anna.courses_attached += ['Git']
gena.courses_attached += ['Git']


andrew.rate_lectur(anna, "Git", 10)
andrew.rate_lectur(anna, "Git", 9)
andrew.rate_lectur(anna, "Git", 7)
gena.rate_hw(andrew, "Git", 9)


# print(round(anna.general_values(),1))
# print(anna.grades.values())
print(gena)
print(anna)


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)