class veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}')

class carro(veiculo):
    def exibir_info(self):
        print(f'carro - marca: {self.marca}, modelo: {self.modelo}')

class moto(veiculo):
    def exibir_info(self):
        print(f'moto - marca: {self.marca}, modelo: {self.modelo}')

c = carro('toyota','corolla')
m = moto('honda', 'cb500')
b = veiculo('honda','cb600')

c.exibir_info()
m.exibir_info()
b.exibir_info()
