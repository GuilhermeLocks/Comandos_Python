class Autenticavel:
    def autenticar(self, senha):
        return senha == '1234'

class Registravel:
    def registrar(self):
        print('Usuários registrado com sucesso')

class Usuario(Autenticavel, Registravel):
    def __init__(self, nome):
        self.nome = nome

u = Usuario('Guilherme')
print(u.autenticar('1234'))

u.registrar()