class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def __add__(self, outra_conta):
        return Conta(self.saldo + outra_conta.saldo)

    def __str__(self):
        return f"Saldo: R${self.saldo:.2f}"

c1 = Conta(1000)
c2 = Conta(500)
c3 = c1 + c2
print(c3)
