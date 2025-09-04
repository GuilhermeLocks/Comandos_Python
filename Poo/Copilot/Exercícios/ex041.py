class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, deposito):
        self.deposito = deposito
        self.saldo += self.deposito
        print(f'Saldo :R${self.saldo}, Deposito: R${self.deposito}')

    def sacar(self, sacar):
        self.sacar = sacar
        if self.saldo - self.sacar >= 0:
            self.saldo -= self.sacar
            print(f'Saldo :$R{self.saldo}, Valor sacado :R${self.sacar}')
        else:
            print(f'Saldo insuficiente')
            
class ContaComHistorico(Conta):
    def __init__(self, saldo=0):
        super().__init__(saldo)
        self.historico = []

    def depositar(self, valor):
        super().depositar(valor)
        self.historico.append(f"Depósito: R${valor}")

    def sacar(self, valor):
        if valor <= self.saldo:
            super().sacar(valor)
            self.historico.append(f"Saque: R${valor}")
        else:
            self.historico.append("Tentativa de saque sem saldo")

    def mostrar_historico(self):
        return self.historico


c = ContaComHistorico(500)
c.depositar(100)
c.sacar(200)
print(c.mostrar_historico())