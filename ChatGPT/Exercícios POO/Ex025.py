class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

p = Professor("Carlos", 40, "Matemática")
print(p.nome, p.idade, p.disciplina)
