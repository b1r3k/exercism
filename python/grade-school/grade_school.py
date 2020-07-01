import bisect


class School:
    def __init__(self):
        self._students = tuple()

    def _get_grade_range(self, grade):
        grades = [r[1] for r in self._students]
        left_insort_idx = bisect.bisect_left(grades, grade)
        right_insort_idx = bisect.bisect_right(grades, grade)
        return left_insort_idx, right_insort_idx

    def add_student(self, name, grade):
        left_insort_idx, right_insort_idx = self._get_grade_range(grade)
        names = [r[0] for r in self._students]
        students = list(self._students)
        left_name_insort_idx = bisect.bisect_left(names, name, left_insort_idx, right_insort_idx)
        students.insert(left_name_insort_idx, (name, grade))
        self._students = tuple(students)

    def roster(self):
        r = []
        for name, grade in self._students:
            r.append(name)
        return r

    def grade(self, grade_number):
        left_insort_idx, right_insort_idx = self._get_grade_range(grade_number)
        students_in_grade = list(name for name, grade in self._students[left_insort_idx:right_insort_idx])
        return students_in_grade
