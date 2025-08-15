class usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def aluno(self):
        print(f'Nome: {self.nome}')
        print(f'Email: {self.email}')

    def professor(self):
        print(f'Nome: {self.nome}')
        print(f'Email: {self.email}')

usuario('nome 1', 'email 1').aluno()
usuario('nome 2', 'email 2').professor()