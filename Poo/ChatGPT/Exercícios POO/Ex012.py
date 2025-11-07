class Pai:
    def falar(self):
        print('Conselhos sérios')

class Mae:
    def cuidar(self):
        print('Muito carinho')

class Filho(Pai, Mae):
    pass

f = Filho()
f.falar()
f.cuidar()