import hashlib

class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, senha):
        self.__hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()

    def validar(self, chave):
        self.chave = hashlib.sha256(chave.encode('utf-8')).hexdigest()
        if self.chave == self.__hash:
            print('Senha validada!')
        else:
            print('Senha invalida!')
        print(f'Senha: {self.__hash}')
        print(f'Chave: {self.chave}')

c = Credencial()
c.senha = input('Digite a senha: ')
c.validar(input('Digite a chave: '))
