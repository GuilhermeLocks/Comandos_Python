class ContaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        print(f'Valor depositado: R${valor:.2f}')

    def ver_saldo(self):
        return f'Saldo: R${self._saldo:.2f}'

c = ContaBancaria(100)
c.depositar(100)
print(c.ver_saldo())