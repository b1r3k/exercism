
STUDENTS = ('Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid',
            'Larry')


class Garden:
    plants_types = ['grass', 'clover', 'radishes', 'violets']
    cup_to_plant = {plant_type[0].upper(): plant_type.capitalize() for plant_type in plants_types}

    def __init__(self, diagram, students=None):
        self._students_plants = self.student_to_plants(diagram.splitlines(), sorted(students or STUDENTS))

    def student_to_plants(self, diagram, students):
        students2plant = {}
        all_students_plants = {}
        col = 0
        for student in students:
            students_plants = students2plant.setdefault(student, [])
            students_plants.extend(diagram[0][col:col + 2])
            students_plants.extend(diagram[1][col:col + 2])
            all_students_plants[student] = [self.cup_to_plant[cup] for cup in students2plant[student]]
            col += 2
        return all_students_plants

    def plants(self, student):
        return self._students_plants.get(student)
