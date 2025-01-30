class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Метод выставления оценок лекторам
    def rate_speaker(self, speaker, course, grade_speaker):
        if isinstance(speaker, Lecturer) and course in speaker.courses_attached and course in self.courses_in_progress:
            if course in speaker.grades:    
                speaker.grades[course].append(grade_speaker)
            else:
                speaker.grades[course] = [grade_speaker]
        else:
            return 'Ошибка'

    # Метод вычисления средней оценки за лекции   
    def average_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count > 0 else 0
    
    # Перегрузка метода
    def __str__(self):
        return (f'\n'
                f'Студент\n'
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade():.1f}\n'
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

    # Метод вычисления средней оценки за лекции
    def average_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count > 0 else 0
    
    def __str__(self):
        return (f'Лектор\n'
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade():.1f}\n')


    # Задание № 1. -Создаём класс-наследник от Mentor - Reviewer (эксперты, проверяющие домашние задания)
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

        # Создаём метод выставления оценок студентам
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f'Проверяющий\n'
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')


best_student_1 = Student('Ruoy', 'Eman', 'your_gender')
best_student_1.courses_in_progress += ['Python', 'Java']
best_student_1.finished_courses = ['Введение в программирование']

best_student_2 = Student('Elvis', 'Presley', 'your_gender')
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
 

print(best_student_1)
print(best_student_2)
print(cool_reviever_1)
print(cool_reviever_2)
print(cool_speaker_1)
print(cool_speaker_2)


# и для этих студентов, лекторов, ревьюверов вывести через print атрибуты и методы (просто визуализировать, что код рабочий)
# А также написать две функции (одну для студентов, другую для лекторов), которые берут на вход принимать:
# список студенотов и предмет('Git' например)
# вход:
# st_list = [student_1, student_2]
# по типу:
# def all_st_gr_average(st_list, 'Git')

# а на выходе:
# f'Средняя оценка по курсу {ttl_course} для всех лекторов: {round(sum_av_all / q_lr, 1)}
# или сообщать, что нет оценок на данном курсе