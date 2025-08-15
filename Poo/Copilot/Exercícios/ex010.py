class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class livro(produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

class electronica(produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

class roupa(produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

class carrinho(livro, electronica, roupa):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)
            