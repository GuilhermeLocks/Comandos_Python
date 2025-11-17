class Estoque:
    def __init__(self):
        self.itens = {}

    def adicionar(self, item, qtde):
        self.itens[item] = self.itens.get(item, 0) + qtde

e = Estoque()
e.adicionar('Maça', 5)
e.adicionar('Maça', 3)
print(e.itens)