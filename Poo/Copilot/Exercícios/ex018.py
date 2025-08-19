from datetime import datetime

class Veiculo:
    def __init__(self, placa, ano):
        self.placa = placa
        self.ano = ano

class Carro(Veiculo): pass
class Moto(Veiculo): pass
class Caminhao(Veiculo): pass

class Frota:
    def __init__(self):
        self.veiculos = []

    def adicionar(self, veiculo):
        self.veiculos.append(veiculo)

    def idade_media(self):
        atual = datetime.now().year
        return sum(atual - v.ano for v in self.veiculos) / len(self.veiculos)

f = Frota()
f.adicionar(Carro("ABC1234", 2018))
f.adicionar(Moto("XYZ5678", 2020))
print(f"Idade média da frota: {f.idade_media():.1f} anos")