class Veiculo:
    def __init__(self, modelo, km_por_litro):
        self.modelo = modelo
        self.km_por_litro = km_por_litro

    def calcular_consumo(self, distancia):
        self.distancia = distancia
        return self.distancia / self.km_por_litro

class Carro(Veiculo): pass
class Moto(Veiculo): pass

v = Moto("CG 160", 40)

print(f'{v.modelo} - Consumo em 200km: {v.calcular_consumo}')