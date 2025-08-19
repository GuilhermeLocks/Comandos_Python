class usuaria:
    def __init__(self, nome, remetente, destinatario, texto):
        self.nome = nome
        self.remetente = remetente
        self.destinatario = destinatario
        self.texto = texto

class aluno(usuaria): pass
class professor(usuaria): pass

class mensagem(aluno):
    def aluno(self):
        print(f'aluno: {self.nome}, remetente: {self.remetente}, destinatario: {self.destinatario}, texto: {self.texto}')

    def professor(self):
        print(f'professor: {self.nome}, remetente: {self.remetente}, destinatario: {self.destinatario}, texto: {self.texto}')

mensagem('1', '2', '3', '4').aluno()
mensagem('1', '2', '3', '4').professor()