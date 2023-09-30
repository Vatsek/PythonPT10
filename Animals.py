# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
class Animal:
    def __init__(self, name: str, age: int, *args):
        self.name = name
        self.age = age
        self.spec = None or 'не определены'

    def get_spec(self):
        return self.spec

    def __str__(self):
        return f'Класс: {type(self).__name__}\nИмя: {self.name}\nвозраст: {self.age}\nнавыки: {self.spec}\n'


class Dog(Animal):
    def __init__(self, name: str, age: int, spec=None):
        super().__init__(name, age)
        self.spec = spec if spec else 'не определены'

    def __str__(self):
        return f'Класс: {type(self).__name__}\nИмя: {self.name}\nвозраст: {self.age}\nнавыки: {self.spec}\n'


class Fish(Animal):
    def __init__(self, name: str, age: int, spec=None):
        super().__init__(name, age)
        self.spec = spec if spec else 'не определены'

    def __str__(self):
        return f'Класс: {type(self).__name__}\nИмя: {self.name}\nвозраст: {self.age}\nнавыки: {self.spec}\n'


class Bird(Animal):
    def __init__(self, name: str, age: int, spec=None):
        super().__init__(name, age)
        self.spec = spec if spec else 'не определены'

    def __str__(self):
        return f'Класс: {type(self).__name__}\nИмя: {self.name}\nвозраст: {self.age}\nнавыки: {self.spec}\n'


if __name__ == '__main__':
    d1 = Dog('Полкан', 3, 'гавкает')
    f1 = Fish('Немо', 1, 'плывёт')
    b1 = Bird('Чирик', 2, 'поет')
