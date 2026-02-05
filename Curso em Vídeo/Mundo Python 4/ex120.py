from rich.panel import Panel
from rich import print
               
lista_de_jogos = []

class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick

    def add_favoritos(self, jogo):
        lista_de_jogos.append(jogo)

    def ficha(self):
        lista_de_jogos.sort()
        produto = Panel(f'Nome real: {self.nome}'
                        f'\nJogos favoritos:'
                        f'\n{lista_de_jogos}', title=f'Jogador <{self.nick}>')
        print(produto)

j1 = Gamer('Naruto', 'Nana')
j1.add_favoritos('c')
j1.add_favoritos('b')
j1.add_favoritos('a')
j1.ficha()