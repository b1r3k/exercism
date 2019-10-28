class Garden:
    STUDENTS = ('Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid',
                'Larry')
    CUP_TO_PLANT = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

    def __init__(self, diagram, students=None):
        self._students = sorted(students or self.STUDENTS)
        self._students_plants = self.student_to_plants(diagram.splitlines(), self._students)

    def student_to_plants(self, diagram, students):
        all_students_plants = {}
        col = 0
        for student in students:
            students_plants = all_students_plants.setdefault(student, [])
            first_row_cups = diagram[0][col:col + 2]
            second_row_cups = diagram[1][col:col + 2]
            students_plants.extend(self.CUP_TO_PLANT[cup] for cup in first_row_cups)
            students_plants.extend(self.CUP_TO_PLANT[cup] for cup in second_row_cups)
            col += 2
        return all_students_plants

    def plants(self, student):
        return self._students_plants.get(student)
