class contabancaria:

    def __init__(self):
        self.saldo = 0

    def depositar(self, deposito):
        self.deposito = deposito
        self.saldo += self.deposito
        print(f'saldo: {self.saldo}, deposito: {self.deposito}')

    def sacar(self, sacar):
        self.sacar = sacar
        if self.saldo >= self.sacar:
            self.saldo -= self.sacar
            print(f'saldo: {self.saldo}, sacado: {self.sacar}')
        else:
            print('Saldo insuficiente')

    def saldo(self):
        print(self.saldo)

cb = contabancaria()

cb.depositar(1000)

cb.sacar(100)