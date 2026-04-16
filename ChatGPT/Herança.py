class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print('Som genérico de animal')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome

    def falar(self):
        print(f'{self.nome} falou Au Au!')

class Gato(Animal):
    def falar(self):
        print('Miau!')

dog = Cachorro('Rex')
cat = Gato('Mimi')
pato = Animal('Pato')

dog.falar()
cat.falar()
pato.falar()

