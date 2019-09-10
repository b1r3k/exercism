
STUDENTS = ('Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid',
            'Larry')


class Garden(object):
    plants_types = ['grass', 'clover', 'radishes', 'violets']
    cup_to_plant = {plant_type[0].upper(): plant_type.capitalize() for plant_type in plants_types}

    def __init__(self, diagram, students=None):
        self._students_plants = self.student_to_plants(diagram.split('\n'), sorted(students or STUDENTS))

    def student_to_plants(self, diagram, students):
        students2plant = {}
        all_students_plants = {}
        for student_idx, col_start in enumerate(range(0, len(diagram[0]), 2)):
            students_plants = students2plant.setdefault(students[student_idx], [])
            students_plants.append(diagram[0][col_start])
            students_plants.append(diagram[0][col_start + 1])
            students_plants.append(diagram[1][col_start])
            students_plants.append(diagram[1][col_start + 1])
        for student in students:
            all_students_plants[student] = [self.cup_to_plant[cup] for cup in students2plant.get(student, [])]
        return all_students_plants

    def plants(self, student):
        return self._students_plants.get(student)
