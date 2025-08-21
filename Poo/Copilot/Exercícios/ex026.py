class veiculo:
    def __init__(self, modelo):
        self.modelo = modelo

class eletrico(veiculo):
    def __init__(self, modelo, autonomia):
        super().__init__(modelo)
        self.autonomia = autonomia

    def carregar(self):
        return f'Modelo: {self.modelo}, Autonomia: {self.autonomia}'

v = eletrico("Tesla Model 3", 400)
print(v.carregar())