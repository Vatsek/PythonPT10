from Animals import Animal, Dog, Fish, Bird


class Factory:

    def create(type_of_animal: str, name: str, age=0, spec=None):
        if type_of_animal == 'Dog':
            return Dog(name, age, spec)
        elif type_of_animal == 'Fish':
            return Fish(name, age, spec)
        elif type_of_animal == 'Bird':
            return Bird(name, age, spec)
        else:
            return Animal(name, age, spec)
