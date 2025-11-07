class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def saldo(self):
        print(f'Saldo: {self.saldo}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
        else:
            print('Saldo insuficiente')

conta = ContaBancaria('Guilherme', 500)
conta.depositar(100)
conta.sacar(700)
print(f'Saldo: {conta.saldo}')