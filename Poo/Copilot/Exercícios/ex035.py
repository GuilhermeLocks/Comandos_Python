class funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class gerente(funcionario):
    def bonus(self):
        print(f'O funcionario {self.nome} com o cargo gerente tem o saladio de R${(self.salario):.2f} com o bonus de 30% firaca R${(self.salario * 1.30):.2f} ')

class analista(funcionario):
    def bonus(self):
        print(f'O funcionario {self.nome} com o cargo analista tem o saladio de R${(self.salario):.2f} com o bonus de 20% firaca R${(self.salario * 1.20):.2f} ')

class estagiario(funcionario):
    def bonus(self):
        print(f'O funcionario {self.nome} com o cargo estagiario tem o saladio de R${(self.salario):.2f} com o bonus de 10% firaca R${(self.salario * 1.10):.2f} ')

gerente('Nome', 1000).bonus()
analista('Nome', 1000).bonus()
estagiario('Nome', 1000).bonus()