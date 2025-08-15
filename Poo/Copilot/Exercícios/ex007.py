class funcionario:
    def calcular_bonus(self):
        return 1000

class gerente:
    def calcular_bonus(self):
        return 3000

class estagiario:
    def calcular_bonus(self):
        return 500

lista = [funcionario(), gerente(), estagiario()]

for pessoa in lista:
    print(f'Bônus: R${pessoa.calcular_bonus()}')