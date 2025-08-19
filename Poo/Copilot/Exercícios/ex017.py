class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Aluno(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def media(self):
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        return "Aprovado" if self.media() >= 7 else "Reprovado"

a = Aluno("João")
a.adicionar_nota(8)
a.adicionar_nota(6)
print(f"{a.nome} - Média: {a.media():.2f} - {a.situacao()}")