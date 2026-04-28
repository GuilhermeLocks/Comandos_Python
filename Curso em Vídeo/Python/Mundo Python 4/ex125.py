from abc import ABC, abstractmethod
class Trransporte :
    def __init__(self, distancia, tamanho):
        self.distancia = distancia
        self.tamanho = tamanho

    @abstractmethod
    def calc_frete(self):
        pass


class Motor(Trransporte):
    def __init__(self, distancia):
        super().__init__(self, distancia)
        self.distancia = distancia
        self.fator = 0.50

        Motor.calc_frete(self)

    def calc_frete(self):
        self.valor = self.fator * self.distancia
        print(f'Frete de Moto em {self.distancia}Km = R${self.valor:.2f}')

class Caminhao(Trransporte):
    def __init__(self, distancia):
        super().__init__(self, distancia)
        self.distancia = distancia
        self.fator = 1.20

        Caminhao.calc_frete(self)

    def calc_frete(self):
        if self.distancia < 50:
            print(f'Frete de caminhao em {self.distancia}Km = Raio minimo de 50Km')
        else:
            self.valor = self.fator * self.distancia
            print(f'Frete de caminhao em {self.distancia}Km = R${self.valor:.2f}')

class Drone(Trransporte):
    def __init__(self, distancia):
        super().__init__(self, distancia)
        self.distancia = distancia
        self.fator = 9.50

        Drone.calc_frete(self)

    def calc_frete(self):
        if self.distancia > 10:
            print(f'Frete de Drone em {self.distancia}Km = Raio maximo de 10Km')
        else:
            self.valor = self.fator * self.distancia
            print(f'Frete de Drone em {self.distancia}Km = R${self.valor:.2f}')

class Viagem():
    print('oi')

dist = 8
entrega = Drone(dist)

Viagem()