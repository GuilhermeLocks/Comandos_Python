class Animal:
    def mover(self):
        print('Movendo...')

class Peixe(Animal):
    def mover(self):
        super().mover()
        print('Nadando...')

p = Peixe()
p.mover()