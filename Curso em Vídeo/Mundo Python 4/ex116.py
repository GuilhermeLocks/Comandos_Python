from rich import print
class funcionarioa:

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = 'Curso em Video'

    def apresentar(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}'

c1 = funcionarioa('Maria', 'Administração', 'Diretora')
print(c1.apresentar())

c1 = funcionarioa('Pedro', 'TI', 'Programador')
print(c1.apresentar())