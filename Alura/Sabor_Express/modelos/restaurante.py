from Alura.Sabor_Express.modelos.avaliacao import Avaliacao

class Restaurante:
    restarantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restarantes.append(self)

    def __str__(self):
        return f'{self.nome} / {self.categoria}'

    @classmethod
    def listar_restauramtes(cls):
        print(f'{'nome ':<19}{'/categoria ':<20}{'/status':<20}{'/Media':<20}')
        for restaurante in cls.restarantes:
            print(f'{restaurante.nome:<19}/{restaurante.categoria:<19}/{restaurante.ativo:<19}/{restaurante.media_avaliacoes:<20}')

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'falso'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media




    def adicionar_bebida_no_cardapio(self, bebida):
        self._cardapio.append(bebida)

    def adicionar_prato_no_cardapio(self, prato):
        self._cardapio.append(prato)

# restaurante_placa = Restaurante('praça', 'Gourmet')
# restaurante_placa.alternar_estado()
# restaurante_pizza = Restaurante('pizza', 'Italiana')
#
# restaurante_placa.receber_avaliacao('Gui', 5)
# restaurante_placa.receber_avaliacao('Gui', 2)
# restaurante_pizza.receber_avaliacao('Gui', 5)
# restaurante_pizza.receber_avaliacao('Gui', 4)
#
# Restaurante.listar_restauramtes()

# restaurantes = [restaurante_placa, restaurante_pizza]
# print(vars(restaurante_placa))
# print(dir(restaurante_placa))
# print(restaurante_placa)
# for c in restaurantes:
#     print(c)
# print(restaurante_placa.media_avaliacoes)


