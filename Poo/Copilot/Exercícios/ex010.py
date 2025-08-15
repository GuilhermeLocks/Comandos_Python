class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor

class Eletronico(Produto):
    def __init__(self, nome, preco, marca):
        super().__init__(nome, preco)
        self.marca = marca

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, produto):
        self.itens.append(produto)

    def total(self):
        return sum(p.preco for p in self.itens)

c = Carrinho()
c.adicionar(Livro("Python", 50, "Guido"))
c.adicionar(Eletronico("Fone", 120, "Sony"))
print(f"Total da compra: R${c.total()}")
