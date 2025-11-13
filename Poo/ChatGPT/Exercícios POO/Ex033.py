class Funcionario:
    def trabalhar(self):
        return 'Funcionario trabalhando'

class Gerente(Funcionario):
    def trabalhar(self):
        super().trabalhar()
        return 'Geremte trabalhando'

f = Funcionario()
g = Gerente()
print(f.trabalhar())
print(g.trabalhar())