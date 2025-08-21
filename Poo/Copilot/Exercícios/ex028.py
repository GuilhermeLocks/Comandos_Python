class usuario:
    def __init__(self, nome):
        self.nome = nome

    def permissao(self):
        return f'{self.nome} tem permissão de leito'

class admin(usuario):
    def permissao(self):
        return f'{self.nome} tem permissão de administrador'

us = usuario('nome1')
print(us.permissao())

ad = admin('nome2')
print(ad.permissao())