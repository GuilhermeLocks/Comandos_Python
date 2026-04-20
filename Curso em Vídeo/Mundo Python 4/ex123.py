class Poligono:
    def __init__(self, qtd_lados, perimetro, area):
        self.qtdLados = qtd_lados
        self.perimetro = perimetro
        self.area = area

class Quadrado(Poligono):

    def calcular_area(self):
        return (self.lado * self.lado)

    def calcular_perimeto(self):
        return (self.lado * 4)

    def __init__(self, lado):
        self.lado = lado
        print(f'Perimento = {self.calcular_perimeto():.1f}')
        print(f'Area = {self.calcular_area():.1f}')

class Circulo(Poligono):
    def calcular_area(self):
        return (3.14 * (self.lado * self.lado))

    def calcular_perimeto(self):
        return (2 * 3.14 * self.lado)

    def __init__(self, lado):
        self.lado = lado
        print(f'Perimento = {self.calcular_perimeto():.1f}')
        print(f'Area = {self.calcular_area():.1f}')

p1 = Quadrado(12)
p2 = Circulo(20)