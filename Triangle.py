class Triangle:
    def __init__(self, a: int | float, b: int | float, c: int | float):
        self.a = a
        self.b = b
        self.c = c
        self.type_triangle = self.determine_type_triangle(self.a, self.b, self.c)

    def __new__(cls, a: int | float, b: int | float, c: int | float):
        if not (a + b < c or b + c < a or c + a < b):
            return object.__new__(cls)
        else:
            return 'Треугольника не существует'

    def determine_type_triangle(self, a, b, c):
        if a == b == c:
            return 'равносторонним'
        elif a == b or b == c or c == a:
            return 'равнобедренным'
        else:
            return 'разносторонним'

    def __str__(self):
        return f'Треугольник со сторонами {self.a}, {self.b}, {self.c} является {self.type_triangle}'


if __name__ == '__main__':
    t1 = Triangle(1, 1, 1)
    t2 = Triangle(1, 2, 3)
    t3 = Triangle(3, 5, 5)
    t4 = Triangle(10, 1, 1)

    print(t1)
    print(t2)
    print(t3)
    print(t4)
