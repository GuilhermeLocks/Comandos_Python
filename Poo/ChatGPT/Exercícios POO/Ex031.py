class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __eq__(self, outro):
        return self.idade == outro.idade

p1 = Pessoa("Ana", 25)
p2 = Pessoa('Bruno', 25)
p3 = Pessoa('Carlos', 30)

print(p1 == p2)
print(p1 == p3)