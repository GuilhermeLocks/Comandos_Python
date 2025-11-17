class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def meu_carro(self):
        return self.marca, self.modelo, self.ano

c=Carro('marca', 'modelo', 'ano')
print(c.meu_carro())