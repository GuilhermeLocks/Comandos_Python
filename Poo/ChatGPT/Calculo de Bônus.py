class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        print( self.salario * 0.10)

class Gerente(Funcionario):
    def calcular_bonus(self):
        print( self.salario * 0.20)

f = Funcionario('Ana', 5000)
g = Gerente('Carlos', 8000)

f.calcular_bonus()
g.calcular_bonus()