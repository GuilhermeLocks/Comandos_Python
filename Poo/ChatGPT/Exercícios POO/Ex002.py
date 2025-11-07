class ContaBancaria:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            print('Saldo insuficiente')

    def ver_saldo(self):
        return self._saldo

conta = ContaBancaria()
conta.depositar(200)
conta.sacar(50)
print(conta.ver_saldo())