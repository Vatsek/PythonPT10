
class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix

    def show_matrix(self):
        for i in self.matrix:
            for j in i:
                print(f'{j:^{3}}', end='')
            print()
        print()

    def matrix_transposition(self):
        new_matrix = []
        rows = len(self.matrix[0])
        columns = len(self.matrix)
        for i in range(rows):
            new_matrix.append([])
            for j in range(columns):
                new_matrix[i].append(0)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                new_matrix[j][i] = self.matrix[i][j]
        self.matrix = new_matrix


if __name__ == '__main__':
    m = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    m.show_matrix()
    m.matrix_transposition()
    m.show_matrix()
