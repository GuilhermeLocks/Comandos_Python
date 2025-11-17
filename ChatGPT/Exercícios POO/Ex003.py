class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir(self):
        return f'nome: {self.nome}, idade: {self.idade}'

p = Pessoa('Jorge', '18')
print(p.exibir())
