import bisect


class Student:
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    @property
    def name(self):
        return self._name

    @property
    def grade(self):
        return self._grade

    def __lt__(self, other):
        if self._grade < other.grade:
            return True
        if self._grade == other.grade and self._name < other.name:
            return True

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '{} {}'.format(self._grade, self._name)


class School:
    def __init__(self):
        self._students = tuple()

    def add_student(self, name, grade):
        student = Student(name, grade)
        students = list(self._students)
        bisect.insort(students, student)
        self._students = tuple(students)

    def roster(self):
        return [student.name for student in self._students]

    def grade(self, grade_number):
        students_in_grade = list(student.name for student in self._students if student.grade == grade_number)
        return students_in_grade
