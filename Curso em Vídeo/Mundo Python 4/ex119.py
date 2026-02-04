from rich import print
from time import sleep
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f'[blue]Você acabou de abrir o Livro [red]{self.titulo}[blue] que tem [green]{self.paginas} paginas[blue] no total. Você agora está na [yellow]página 1')

    def avancar_paginas(self, avancar):
        self.avancar= avancar
        cont = 0
        if self.pagina_atual + self.avancar <= self.paginas:
            for c in range(self.pagina_atual+1, (self.pagina_atual+self.avancar)+1):
                print(f'Pág{c}> ', end='')
                cont += 1
            self.pagina_atual += cont
            print(f'Você avançou {cont} páginas e agora está na página {self.pagina_atual}')
        else:
            for c in range(self.pagina_atual+1, self.paginas+1):
                print(f'Pág{c}> ', end='')
                cont += 1
            self.pagina_atual += cont
            print(f'Você avançou {cont} páginas e agora está na página {self.pagina_atual}')
            if self.pagina_atual == 20:
                print(f'Voce chegou ao final do livro {self.titulo}')

l1 = Livro('10 coisa que aprendi', 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)