class Animal:
    def falar(self):
        print("Som genérico")

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

animais = [Cachorro(), Gato()]
for a in animais:
    a.falar()