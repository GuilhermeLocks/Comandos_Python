class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            print("Erro: temperatura abaixo do zero absoluto!")
        else:
            self._celsius = valor

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

t = Temperatura(25)
print(t.fahrenheit)
t.celsius = -300  # invalido
