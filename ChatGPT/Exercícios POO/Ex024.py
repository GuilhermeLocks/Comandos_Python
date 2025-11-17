class Aluno:
    total_alunos = 0  # atributo de classe

    def __init__(self, nome):
        self.nome = nome
        Aluno.total_alunos += 1

a1 = Aluno("Ana")
a2 = Aluno("Bruno")
print(f"Total de alunos: {Aluno.total_alunos}")
