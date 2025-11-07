class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Turma:
    def __init__(self):
        self.alunos = []

    def add_aluno(self, aluno):
        self.alunos.append(aluno)

t = Turma()
t.add_aluno(Aluno('Maria'))
t.add_aluno(Aluno('Lucas'))
for alunos in t.alunos:
    print(alunos.nome)