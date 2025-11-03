class Animal:
    def falar(self):
        print('Som genérico')

class Cachorro(Animal):
    def falar(self):
        print('Au Au')

dog = Cachorro()
dog.falar()