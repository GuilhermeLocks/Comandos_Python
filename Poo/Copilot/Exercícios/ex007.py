class Funcionario:
    def calcular_bonus(self):
        return 1000

class Gerente(Funcionario):
    def calcular_bonus(self):
        return 3000

class Estagiario(Funcionario):
    def calcular_bonus(self):
        return 500

lista = [Funcionario(), Gerente(), Estagiario()]
for pessoa in lista:
    print(f"Bônus: R${pessoa.calcular_bonus()}")