from Alura.Sabor_Express.modelos.avaliacao import Avaliacao
from Alura.Sabor_Express.modelos.cardapio.item_carpadio import ItemCardapio

class Restaurante:
    restarantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restarantes.append(self)

    def __str__(self):
        return f'{self._nome} / {self.categoria}'

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

    def adicionar_no_cardapio(self, item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Carddapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):

            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome:{item._nome:<20} / Preço: R${item._preco:<20} /  Descrição:{item.descricao:<20}'
                print(mensagem_prato)
            if hasattr(item, 'tamanho'):
                mensagem_bebida = f'{i}. Nome:{item._nome:<20} / Preço: R${item._preco:<20} /  Descrição:{item.tamanho:<20}'
                print(mensagem_bebida)

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


