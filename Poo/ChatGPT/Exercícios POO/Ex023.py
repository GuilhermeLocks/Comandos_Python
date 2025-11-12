class Motor:
    def funcionar(self):
        print("O motor está funcionando...")

class Carro:
    def __init__(self):
        self.motor = Motor()

    def ligar(self):
        print("Ligando o carro...")
        self.motor.funcionar()

c = Carro()
c.ligar()
