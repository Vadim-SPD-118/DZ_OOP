class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_speaker(self, speaker, course, grade_speaker):
        if isinstance(speaker, Lecturer) and course in speaker.courses_attached and course in self.courses_in_progress:
            speaker.grades.setdefault(course, []).append(grade_speaker)
        else:
            return 'Ошибка'

    def average_grade(self):
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return total / count if count > 0 else 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()
    
    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __str__(self):
        return (f'Студент\n'
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Пол: {self.gender}\n'
                f'Средняя оценка: {self.average_grade():.1f}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return total / count if count > 0 else 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()
    
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __str__(self):
        return (f'Лектор\n'
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка: {self.average_grade():.1f}\n')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f'Проверяющий\n'
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')

# Создание объектов
best_student_1 = Student('Ruoy', 'Eman', 'муж')
best_student_1.courses_in_progress += ['Python', 'Java']
best_student_1.finished_courses = ['Введение в программирование']

best_student_2 = Student('Elvis', 'Presley', 'муж')
best_student_2.courses_in_progress += ['Python', 'Java']
best_student_2.finished_courses = ['Git']
 
cool_reviever_1 = Reviewer('Some', 'Buddy')
cool_reviever_1.courses_attached += ['Python', 'Java']

cool_reviever_2 = Reviewer('Louis', 'Armstrong')
cool_reviever_2.courses_attached += ['Python', 'Java']

cool_speaker_1 = Lecturer('Harry', 'James')
cool_speaker_1.courses_attached += ['Python', 'Java']

cool_speaker_2 = Lecturer('Billie', 'Holyday')
cool_speaker_2.courses_attached += ['Python', 'Java']

# Оценка студентов и лекторов
cool_reviever_1.rate_hw(best_student_1, 'Python', 8)
cool_reviever_1.rate_hw(best_student_1, 'Python', 5)
cool_reviever_1.rate_hw(best_student_1, 'Java', 10)
cool_reviever_1.rate_hw(best_student_1, 'Java', 9)

cool_reviever_2.rate_hw(best_student_2, 'Python', 7)
cool_reviever_2.rate_hw(best_student_2, 'Python', 8)
cool_reviever_2.rate_hw(best_student_2, 'Java', 9)
cool_reviever_2.rate_hw(best_student_2, 'Java', 10)

best_student_1.rate_speaker(cool_speaker_1, 'Python', 10)
best_student_1.rate_speaker(cool_speaker_1, 'Python', 8)
best_student_1.rate_speaker(cool_speaker_1, 'Java', 10)
best_student_1.rate_speaker(cool_speaker_1, 'Java', 9)

best_student_2.rate_speaker(cool_speaker_2, 'Python', 10)
best_student_2.rate_speaker(cool_speaker_2, 'Python', 10)
best_student_2.rate_speaker(cool_speaker_2, 'Java', 10)
best_student_2.rate_speaker(cool_speaker_2, 'Java', 9)

# Вывод результатов
print(best_student_1)
print(best_student_2)
print(cool_reviever_1)
print(cool_reviever_2)
print(cool_speaker_1)
print(cool_speaker_2)

# Сравнение лекторов
if cool_speaker_1 > cool_speaker_2:
    print(f'{cool_speaker_1.name} {cool_speaker_1.surname} лучше, чем {cool_speaker_2.name} {cool_speaker_2.surname}')
elif cool_speaker_1 < cool_speaker_2:
    print(f'{cool_speaker_2.name} {cool_speaker_2.surname} лучше, чем {cool_speaker_1.name} {cool_speaker_1.surname}')
else:
    print(f'{cool_speaker_1.name} {cool_speaker_1.surname} и {cool_speaker_2.name} {cool_speaker_2.surname} имеют одинаковую среднюю оценку')

# Сравнение студентов
if best_student_1 > best_student_2:
    print(f'{best_student_1.name} {best_student_1.surname} лучше, чем {best_student_2.name} {best_student_2.surname}')
elif best_student_1 < best_student_2:
    print(f'{best_student_2.name} {best_student_2.surname} лучше, чем {best_student_1.name} {best_student_1.surname}')
else:
    print(f'{best_student_1.name} {best_student_1.surname} и {best_student_2.name} {best_student_2.surname} имеют одинаковую среднюю оценку')


def average_student_grade(students, course):
    total = 0
    count = 0
    
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    
    return total / count if count > 0 else 0

def average_lecturer_grade(lecturers, course):
    total = 0
    count = 0
    
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    
    return total / count if count > 0 else 0

# Проверка работы функций
students = [best_student_1, best_student_2]
lecturers = [cool_speaker_1, cool_speaker_2]

# Подсчет средней оценки за домашние задания по курсу 'Python'
avg_student_grade_python = average_student_grade(students, 'Python')
print(f'Средняя оценка за домашние задания по курсу "Python": {avg_student_grade_python:.1f}')

# Подсчет средней оценки за лекции по курсу 'Python'
avg_lecturer_grade_python = average_lecturer_grade(lecturers, 'Python')
print(f'Средняя оценка за лекции по курсу "Python": {avg_lecturer_grade_python:.1f}')