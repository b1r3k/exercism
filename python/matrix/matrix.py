class Matrix(object):
    def __init__(self, matrix_string):
        rows = matrix_string.splitlines()
        self._matrix = [[int(col) for col in row.split()] for row in rows]

    def row(self, index):
        return self._matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self._matrix]
