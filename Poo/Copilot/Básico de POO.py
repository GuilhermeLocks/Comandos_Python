class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}, e tenho {self.idade}  anos.')

p1 = Pessoa('Guilherme', 25)
p2 = Pessoa('Ana', 30)

p1.apresentar()
p2.apresentar()
