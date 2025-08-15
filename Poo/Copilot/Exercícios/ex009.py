class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Aluno(Usuario):
    def __init__(self, nome, email, matricula):
        super().__init__(nome, email)
        self.matricula = matricula

class Professor(Usuario):
    def __init__(self, nome, email, disciplina):
        super().__init__(nome, email)
        self.disciplina = disciplina

class Sistema:
    def __init__(self):
        self.usuarios = []

    def cadastrar(self, usuario):
        self.usuarios.append(usuario)

    def listar(self):
        for u in self.usuarios:
            print(f"{u.nome} - {u.email}")

s = Sistema()
s.cadastrar(Aluno("João", "joao@email.com", "123"))
s.cadastrar(Professor("Maria", "maria@email.com", "Matemática"))
s.listar()