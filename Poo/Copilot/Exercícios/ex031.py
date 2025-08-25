class veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class carro(veiculo):
    def categoria(self):
        print(f'Categoria do veiculo: carro, marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}')

class moto(veiculo):
    def categoria(self):
        print(f'Categoria do veiculo: moto, marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}')

class caminhao(veiculo):
    def categoria(self):
        print(f'Categoria do veiculo: caminhao, marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}')

carro("Fiat", "Argo", 2022).categoria()
