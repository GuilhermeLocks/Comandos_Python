from abc import ABC, abstractmethod

class forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class circulo(forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * (self.raio ** 2)

class quadrado(forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class dois(forma):
    def __init__(self, valor):
        self.valor = valor

    def calcular_area(self):
        return self.valor * 2

formas = [circulo(5), quadrado(4), dois(6)]
for f in formas:
    print(f'Área: {f.calcular_area():.2f}')