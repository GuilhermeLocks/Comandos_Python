class Funcionario:
    total = 0

    def __init__(self, nome):
        self.nome = nome
        Funcionario.total += 1

    def quantidade_2(self):
        return Funcionario.total

    @classmethod
    def quantidade(cls):
        return cls.total

f1 = Funcionario('Ana')
f2 = Funcionario('João')
print(Funcionario.quantidade_2(''))
print(Funcionario.quantidade())
