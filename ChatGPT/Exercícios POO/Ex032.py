class Veiculo:
    def acelerar(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        return 'Acelera som de carro'

class Bicicleta(Veiculo):
    def acelerar(self):
        return 'Acelera som de bicicleta'

c = Carro()
b = Bicicleta()
print(c.acelerar())
print(b.acelerar())