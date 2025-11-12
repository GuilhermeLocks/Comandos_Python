class Terrestre:
    def andar(self):
        print("Andando na terra...")

class Aquatico:
    def nadar(self):
        print("Nadando na água...")

class Sapo(Terrestre, Aquatico):
    pass

s = Sapo()
s.andar()
s.nadar()
