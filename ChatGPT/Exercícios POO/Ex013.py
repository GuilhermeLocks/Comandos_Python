class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.autores = []

    def adicionar_autor(self, nome):
        self.autores.append(nome)

livro = Livro('Python na Prática')
livro.adicionar_autor('Ana')
livro.adicionar_autor('Pedro')
print(livro.autores)