from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):

    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimeto(self):
        pass

class Quadrado(Poligono):

    def calcular_area(self):
        return (self.lado * self.lado)

    def calcular_perimeto(self):
        return (self.lado * self.qtd_lados)

    def __init__(self, lado):
        self.qtd_lados = 4
        self.lado = lado
        print(f'Um quadrado de lado = {self.lado}')
        print(f'Possui um perimento = {self.calcular_perimeto():.1f}')
        print(f'Uma area = {self.calcular_area():.1f}\n')

class Circulo(Poligono):

    def calcular_area(self):
        return (pi * (self.raio * self.raio))

    def calcular_perimeto(self):
        return (2 * pi * self.raio)

    def __init__(self, raio):
        self.raio = raio
        print(f'Um circulo de raio = {self.raio}')
        print(f'Possui um perimento = {self.calcular_perimeto():.1f}')
        print(f'Uma area = {self.calcular_area():.1f}')

p1 = Quadrado(20)
p2 = Circulo(12)