class Nadador:
    def nadar(self):
        print("Nadando...")

class Corredor:
    def correr(self):
        print("Correndo...")

class Triatleta(Nadador, Corredor):
    pass

t = Triatleta()
t.nadar()
t.correr()