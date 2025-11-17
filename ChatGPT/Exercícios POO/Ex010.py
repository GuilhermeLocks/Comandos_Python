from abc import ABC, abstractmethod

class Funcionario(ABC):

    @abstractmethod
    def calcular_salario(self):
        pass

class Vendedor(Funcionario):

    def __init__(self, vendas, comissao):
        self.vendas = vendas
        self.comissao = comissao

    def calcular_salario(self):
        return self.vendas * self.comissao

v = Vendedor(10000, 0.05)
print(v.calcular_salario())
