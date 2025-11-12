class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Livro: {self.titulo} | Autor: {self.autor}"

livro = Livro("Dom Casmurro", "Machado de Assis")
print(livro)
