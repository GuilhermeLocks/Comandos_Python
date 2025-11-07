from Alura.Sabor_Express.modelos.cardapio.item_carpadio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao
    def __str__(self):
        return self._nome
