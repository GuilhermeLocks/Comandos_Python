from rich import print

class Funcionario:

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = 'Curso em Video'

    def apresentar(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}'

c1 = Funcionario('Maria', 'Administração', 'Diretora')
c1.empresa = 'Curso'
print(c1.apresentar())

c1 = Funcionario('Pedro', 'TI', 'Programador')
print(c1.apresentar())