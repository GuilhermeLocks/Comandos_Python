class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá! Meu nome é {self.nome} e tenho {self.idade} anos.')

p = Pessoa('Ana', 25)
p.apresentar()