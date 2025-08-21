class conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def aplicar_taxa(self):
        print(f'Saldo: {self.saldo}', end= ' ')
        self.saldo -= ((self.saldo/100)*2)
        print(f'Saldo: {self.saldo}')

class contapremium(conta):
    def aplicar_taxa(self):
        print(f'Saldo: {self.saldo}', end= ' ')
        self.saldo -= ((self.saldo / 100) * 1)
        print(f'Saldo: {self.saldo}')

c1 = conta(1000)
c2 = contapremium(1000)
c1.aplicar_taxa()
c2.aplicar_taxa()