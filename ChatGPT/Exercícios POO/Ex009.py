class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def desconto(self):
        return f'O produto {self.nome} que custava R${int(self.preco):.2f} com 10% de desconto ficará R${int(self.preco)*0.9:.2f}.'

p = Produto('Notebook', '3000')
print(p.desconto)