from abc import ABC, abstractmethod

class forma_geometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class quadrado(forma_geometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class circulo(forma_geometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio ** 2

formas = [quadrado(4), circulo(3)]
for c in formas:
    print(f'Área: {c.calcular_area()}')