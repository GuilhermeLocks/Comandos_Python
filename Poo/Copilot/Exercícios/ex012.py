class funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class vendedor(funcionario):

    def calcular_comissao(self):
        print(f'{self.nome} tem o salario de R$ {self.salario}, com a comissao de vendedor de 30% seu salario fica {(self.salario/100)*130}')

class gerente(funcionario):

    def calcular_comissao(self):
        print(f'{self.nome} tem o salario de R$ {self.salario}, com a comissao de gerente de 60% seu salario fica {(self.salario/100)*160}')

vendedor('Paula', 2500).calcular_comissao()
gerente('Juliana', 4000).calcular_comissao()
