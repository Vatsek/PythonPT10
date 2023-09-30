from Factory import Factory
from Triangle import Triangle
from Matrix import Matrix

dog1 = Factory.create('Dog', 'Полкан', 2, ['лай', 'сидеть'])
dog2 = Factory.create('Dog', 'Шарик', 5)
fish = Factory.create('Fish', 'Немо', 1, ['есть', 'спать'])
bird = Factory.create('Bird', 'Кеша', 1, ['Летать'])
cat = Factory.create('Cat', 'Барсик', 6)

for an in [dog1, dog2, fish, bird, cat]:
    print(an)

t1 = Triangle(1, 1, 1)
t2 = Triangle(1,2,3)
t3 = Triangle(3, 5, 5)
t4 = Triangle(10, 1, 1)

print(t1)
print(t2)
print(t3)
print(t4)

m = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
m.show_matrix()
m.matrix_transposition()
m.show_matrix()