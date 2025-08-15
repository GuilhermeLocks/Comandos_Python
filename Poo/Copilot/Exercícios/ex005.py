class ContaBancaria:
    def __init__(self):
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor

    def mostrar_saldo(self):
        print(f"Saldo: R${self.__saldo}")

class ContaPoupanca(ContaBancaria):
    def render_juros(self):
        self.depositar(self.__saldo * 0.02)

cp = ContaBancaria()
cp.depositar(1000)
cp.sacar(200)
cp.mostrar_saldo()