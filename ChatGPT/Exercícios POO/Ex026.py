class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print("Au Au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

class Passaro(Animal):
    def falar(self):
        print("Piu Piu!")

animais = [Cachorro(), Gato(), Passaro()]
for a in animais:
    a.falar()
