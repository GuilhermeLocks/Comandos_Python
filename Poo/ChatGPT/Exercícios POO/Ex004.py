class Gato:
    def falar(self):
        return 'Miau!'

class Vaca:
    def falar(self):
        return 'Muuu!'

animais = [Gato(), Vaca()]

for animal in animais:
    print(animal.falar())