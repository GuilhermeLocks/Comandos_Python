from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def preparar(self):
        print('--- Iniciando o Preparo ---')

    def ferver_aguar(self):
        print('1. Fervando água a 100 graus Celsius.')

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def misturar(self):
        print('2. Passando água pressurizada pelo pó de café moído.')

    def servir(self):
        print('3. Serindo em xícara pequena.')
        print('--- Bebida Pronta ---')


class Cha(BebidaQuente):
    def misturar(self):
        print('2. Mergulhar o sachê de ervas na água.')

    def servir(self):
        print('3. Servindo em caneca de porcelana com limão.')
        print('--- Bebida Pronta ---')


class Leite(BebidaQuente):


    def misturar(self):
        print('2. Passando vapor pressurizado pelo bico do leite.')

    def servir(self):
        print('3. Servindo na caneca grande, já com  café.')
        print('--- Bebida Pronta ---')

c3 = Leite()
c3.preparar()
c3.ferver_aguar()
c3.misturar()
c3.servir()



