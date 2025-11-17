class Produto:
    def preco_final(self):
        return 0

class Livro(Produto):
    def __init__(self, preco):
        self.preco = preco

    def preco_final(self):
        return self.preco * 0.9

class Eletronico(Produto):
    def __init__(self, preco):
        self.preco = preco

    def preco_final(self):
        return self.preco * 0.8

produtos = [Livro(100), Eletronico(200)]
for produto in produtos:
    print(int(produto.preco_final()))