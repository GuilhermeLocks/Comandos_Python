class conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

class conta_corrente(conta):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def sacar(self, sacar):
        self.sacar = sacar
        if self.saldo - self.sacar >= 0:
            self.saldo -= self.sacar
            print(f'titular: {self.titular}, saldo: {self.saldo}, valor do saque: {self.sacar}')

    def deposito(self, deposito):
        self.deposito = deposito
        self.saldo += self.deposito
        print(f'titular: {self.titular}, saldo: {self.saldo}, valor do deposito: {self.deposito}')

    def render_juros(self, juros):
        self.juros = juros
        print(f'titular: {self.titular}, saldo: {self.saldo}, valor com juros: {(self.saldo*self.juros)}')

conta_corrente('nome1', 1000).sacar(100)
conta_corrente('nome2', 1000).deposito(100)
conta_corrente('nome2', 1000).render_juros(1.1)