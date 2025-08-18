class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Livro(Produto): pass
class Jogo(Produto): pass
class Filme(Produto): pass

class Loja:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)

    def buscar(self, nome):
        for p in self.produtos:
            if p.nome.lower() == nome.lower():
                return p
        return None

loja = Loja()
loja.adicionar(Livro("Python", 50))
loja.adicionar(Jogo("FIFA", 200))
p = loja.buscar("fifa")
print(f"Produto encontrado: {p.nome} - R${p.preco}")

