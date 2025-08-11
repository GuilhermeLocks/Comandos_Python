class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, cargo, salario):
        super().__init__(nome, cpf)
        self.salario = salario
        self.cargo = cargo

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f'Salario: {self.salario}')
        print(f'Cargo: {self.cargo}')

f1 = Funcionario('Rex', '123.456.789-00', 'Desenvolvedor', 7500.00)
f1.mostrar_dados()
