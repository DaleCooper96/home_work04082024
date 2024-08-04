class Mentor:
    def __init__(self, name, surname, courses=None):
        self.name = name
        self.surname = surname
        self.courses_attached = courses if courses is not None else []

    def attach_course(self, course_name):
        self.courses_attached.append(course_name)

    def detach_course(self, course_name):
        self.courses_attached.remove(course_name)

class Reviewer(Mentor):
    pass

class Lecturer(Mentor):
    def __init__(self, name, surname, courses=None):
        super().__init__(name, surname, courses)
        self.grades = {}  
        
    def rate_students(self, student, course, grade):
        if course in self.courses_attached and course in student.courses_in_progress:
            if course not in self.grades:
                self.grades[course] = [grade]
            else:
                self.grades[course].append(grade)
        else:
            return 'Ошибка'

    @property
    def average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        num_courses = len(self.grades)
        return total_grades / num_courses if num_courses > 0 else 0

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade:.1f}"

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def get_lecturer_grade(self, lecturer, course):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            grades = lecturer.grades.get(course, [])
            return sum(grades) / len(grades)
        else:
            return 'Ошибка'

    def set_lecturer_grade(self, lecturer, course, grade):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    @property
    def average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        num_courses = len(self.grades)
        return total_grades / num_courses if num_courses > 0 else 0

    def __str__(self):
        finished_courses_str = ', '.join(self.finished_courses)
        in_progress_courses_str = ', '.join(self.courses_in_progress)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade:.1f}\nКурсы в процессе изучения: {in_progress_courses_str}\nЗавершенные курсы: {finished_courses_str}"

    def __lt__(self, other):
        return self.average_grade < other.average_grade

def calculate_average_homework_grade(students_list, course_name):
    total_grades = 0
    count_courses = 0
    for student in students_list:
        if course_name in student.courses_in_progress:
            grades = student.grades.get(course_name, [])
            total_grades += sum(grades)
            count_courses += 1
    return total_grades / count_courses if count_courses > 0 else 0

def calculate_average_lecture_grade(lecturers_list, course_name):
    total_grades = 0
    count_courses = 0
    for lecturer in lecturers_list:
        if course_name in lecturer.courses_attached:
            grades = lecturer.grades.get(course_name, [])  # Теперь grades существует
            total_grades += sum(grades)
            count_courses += 1
    return total_grades / count_courses if count_courses > 0 else 0


mentor1 = Lecturer('Some', 'Buddy', ['Python'])
mentor2 = Reviewer('Jane', 'Smith', ['Math'])

student1 = Student('Ruoy', 'Eman', 'your_gender')
student2 = Student('Another', 'Student', 'your_gender')

mentor1.attach_course('Python')
mentor2.attach_course('Math')

mentor1.rate_students(student1, 'Python', 10)
mentor1.rate_students(student1, 'Python', 10)
mentor1.rate_students(student1, 'Python', 10)

student1.set_lecturer_grade(mentor1, 'Python', 7)

avg_homework_grade = calculate_average_homework_grade([student1, student2], 'Python')
avg_lecture_grade = calculate_average_lecture_grade([mentor1, mentor2], 'Python')

print(f"Средняя оценка за домашние задания по курсу Python: {avg_homework_grade:.1f}")
print(f"Средняя оценка за лекции по курсу Python: {avg_lecture_grade:.1f}")

print(mentor1)
print(student1)
print(student2)

print(student1 < student2)
