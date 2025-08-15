class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

class Carro(Veiculo):
    def exibir_info(self):
        print(f"Carro - {self.marca} {self.modelo}")

class Moto(Veiculo):
    def exibir_info(self):
        print(f"Moto - {self.marca} {self.modelo}")

c = Carro("Toyota", "Corolla")
m = Moto("Honda", "CB500")
c.exibir_info()
m.exibir_info()

print()

Carro("Toyota", "Corolla").exibir_info()
Moto("Honda", "CB500").exibir_info()