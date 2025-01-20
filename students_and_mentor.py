class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    # Создаём метод выставления оценок лекторам
    def rate_speaker(self, speaker, course, grade_speaker):
        if isinstance(speaker, Lecturer) and course in speaker.courses_attached and course in self.courses_in_progress:
            if course in speaker.grades_speaker:
                speaker.grades_speaker[course] += [grade_speaker]
            else:
                speaker.grades_speaker[course] = [grade_speaker]
        else:
            return 'Ошибка'

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
      #  self.courses_attached = []
        

        
    # Задание № 1. Создаём класс-наследник от Mentor - Lecturer (лекторы)
class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        self.grades_speaker = {}


    # Задание № 1. -Создаём класс-наследник от Mentor - Reviewer (эксперты, проверяющие домашние задания)
class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        # Создаём метод выставления оценок студентам
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Java']
 
cool_reviever = Reviewer('Some', 'Buddy')
cool_reviever.courses_attached += ['Python', 'Java']

cool_speaker = Lecturer('Harry', 'James')
cool_speaker.courses_attached += ['Python', 'Java']
 
cool_reviever.rate_hw(best_student, 'Python', 10)
cool_reviever.rate_hw(best_student, 'Python', 10)
cool_reviever.rate_hw(best_student, 'Java', 10)

best_student.rate_speaker(cool_speaker, 'Python', 10)
best_student.rate_speaker(cool_speaker, 'Python', 10)
best_student.rate_speaker(cool_speaker, 'Java', 10)
 
print('Оценки студентам:', best_student.grades)

print('Оценки лекторам:',cool_speaker.grades_speaker)




    # def grade_s(self, lecturer, course, grade):
    #     if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
    #         if course in lecturer.grades_f_s:
    #             lecturer.grades_f_s[course] += [grade]
    #         else:
    #             lecturer.grades_f_s[course] = [grade]
    #     else:
    #         return 'Ошибка'





# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}

#         def add_courses(self, course_name):
#    		    self.finished_courses.append(course_name)   

     
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
        
#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python', 'Java']

# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python', 'Java']

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Java', 10)
# cool_mentor.rate_hw(best_student, 'Java', 10)

# print(best_student.grades)


# нужно проставить оценки лекторам по типу:
# student_1.rate_lect(lecturer_1, 'Python', 9)
# student_1.rate_lect(lecturer_1, 'Python', 10)
# student_1.rate_lect(lecturer_1, 'Python', 10)
# и студентам аналогично.

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