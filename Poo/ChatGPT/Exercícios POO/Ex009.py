class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo, motor):
        self.modelo = modelo
        self.motor = motor

motor = Motor(160)
carro = Carro('Sedan', motor)
print(carro.modelo, carro.motor.potencia)