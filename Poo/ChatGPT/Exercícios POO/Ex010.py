class Numero:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, outro):
        return Numero(self.valor + outro.valor)

n1 = Numero(10)
n2 = Numero(20)
resultado = n1 + n2
print(resultado.valor)