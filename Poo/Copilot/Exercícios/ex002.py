class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class funcionario(pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario

f = funcionario('ana', 30, 'engenheira', 7000)
print('nome: ', f.nome)
print('idade: ', f.idade)
print('cargo: ', f.cargo)
print('salario: ', f.salario)