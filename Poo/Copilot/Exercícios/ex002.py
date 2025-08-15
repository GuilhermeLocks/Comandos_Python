class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario

f = Funcionario("Ana", 30, "Engenheira", 7000)
print(f"{f.nome}, {f.idade} anos, Cargo: {f.cargo}, Salário: R${f.salario}")