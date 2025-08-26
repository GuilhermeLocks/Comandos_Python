class conta:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

class conta_corrente(conta):
    def sacar(self, sacar):
        self.sacar = sacar
        if self.saldo + self.limite >= self.sacar:
            if self.saldo - self.sacar >= 0:
                self.saldo -= self.sacar
                print(f'1titular: {self.titular} saldo: {self.saldo} limite: {self.limite} sacar: {self.sacar}')
            else:
                self.saldo -= self.sacar
                self.limite -= self.saldo * -1
                self.saldo = 0
                print(f'2titular: {self.titular} saldo: {self.saldo} limite: {self.limite} sacar: {self.sacar}')
        else:
            print('Saldo insuficiente')
            print(f'titular: {self.titular} saldo: {self.saldo} limite: {self.limite} sacar: {self.sacar}')

conta_corrente('nome', 1000, 1000).sacar(1900)
