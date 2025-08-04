class jogador:
    def __init__(self, altura, velocidade, passe, drible, precisao):
        self.altura = altura
        self.velocidade = velocidade
        self.passe = passe
        self.drible = drible
        self.precisao = precisao

    def passar(self):
        print('Mirar')
        print('Encostar na bola com a força de passe do jogador')

    def chutar(self):
        print('Mirar')
        print('Encocstar na bola com 2x a foça de passe do jogador')

class jogador_goleira(jogador):
    def agarrar(self):
        print('Pular')
        print('Se esticar para pegar a bola')

class jogador_linha(jogador):
    pass

jogador1 = jogador_goleira(180, 60, 80, 20, 60)
jogador2 = jogador_linha(175, 90, 80, 85, 80)

jogador1.passar()
jogador2.passar()
jogador1.agarrar()