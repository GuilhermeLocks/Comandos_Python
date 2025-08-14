class nadador:
    def nadar(self):
        print('nada')

class corredor:
    def correr(self):
        print('corre')

class triatleta(nadador, corredor):
    pass

t = triatleta()
t.nadar()
t.correr()
corredor().correr()
