class Mamifero:
    def amamentar(self):
        print('Amamentar')


class Aquatico:
    def nadar(self):
        print('Nadar')

class Baleia(Mamifero, Aquatico):
    pass

b = Baleia()
b.nadar()
b.amamentar()
