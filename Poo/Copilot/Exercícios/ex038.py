class livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

    def emprestar(self):
        if self.emprestado == True:
            print(f'O {self.titulo} do autor {self.autor} esta emprestado')
        else:
            print(f'O {self.titulo} do autor {self.autor} esta disponivel')
            self.emprestado = True

class livro_fisico(livro): pass
class livro_digital(livro): pass

livro_fisico('titulo 1','auto 1' ).emprestar()
livro_digital('titulo 2','auto 2').emprestar()