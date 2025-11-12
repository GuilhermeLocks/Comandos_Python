class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

class Autor:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        print(f"Livros de {self.nome}:")
        for livro in self.livros:
            print("-", livro.titulo)

a = Autor("Machado de Assis")
a.adicionar_livro(Livro("Dom Casmurro"))
a.adicionar_livro(Livro("Memórias Póstumas"))
a.listar_livros()
