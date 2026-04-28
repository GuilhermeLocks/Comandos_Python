from abc import ABC, abstractmethod
from random import randint
class Personagem(ABC):
    def __init__(self, nome, vida, golpe):
        self.nome = nome
        self.vida = vida
        self.golpe = golpe

    def atacar(self, alvo, forca):
        pass

    def receber_dano(self, dano):
        self.dano = dano
        self.vida -= self.dano

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self, alvo, forca):
        self.dano = alvo
        self.forca = forca
        self.dano = (forca/100)*randint(1, 100)
        p2.vida -= self.dano
        print(f'Kratos({self.vida}) atacou o {p2.nome}({p2.vida}) com um soco de força de {self.forca}')
        print(f'Merlin recebeu dano de {self.dano}')

    def curar(self):
        self.curar = randint(1, 100)
        self.vida += self.curar

        print(f'{self.nome} curou {self.curar}, vida = {self.vida}')


class Mago(Personagem):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def curar(self):
        self.curar = randint(1, 100)
        self.vida += self.curar

        print(f'{self.nome} curou {self.curar}, vida = {self.vida}')

    def atacar(self, alvo, forca):
        self.dano = alvo
        self.forca = forca
        self.dano = (forca/100)*randint(1, 100)
        p1.vida -= self.dano
        print(f'{self.nome}({self.vida}) atacou o {p1.nome}({p1.vida}) com um soco de força de {self.forca}')
        print(f'{p1.nome} recebeu dano de {self.dano}')


p1 = Guerreiro('Kratos', 2000)
p2 = Mago('Merlin', 3000)

p1.atacar(p2, 1000)
p2.curar()
p2.atacar(p1, 2000)
p1.curar()