class usuaria:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def autenticar_senha(self):
        if self.senha == 1234:
            print('Senha esta correta')
        else:
            print('Senha esta incorreta')
class admin(usuaria): pass
class visitante(usuaria): pass

admin('Nome', 1234).autenticar_senha()
visitante('Nome', 123).autenticar_senha()