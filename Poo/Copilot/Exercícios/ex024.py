class animal:
    def __init__(self, nome):
        self.nome = nome

class peixe(animal):
    def alimentar(self):
        print(f'alimentando {self.nome} com comida de peixa')

class passaro(peixe):
    def alimentar(self):
        print(f"alimentando {self.nome} com comida de passaro")

a1 = peixe('nemo')
a2 = passaro('piu')
a1.alimentar()
a2.alimentar()
