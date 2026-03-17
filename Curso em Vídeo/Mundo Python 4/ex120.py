from rich.panel import Panel
from rich import print
               
lista_de_jogos = []

class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick

    def add_favoritos(self, jogo):
        lista_de_jogos.append(jogo)
        lista_de_jogos.sort()

    def ficha(self):

        conteudo = f'Nome real: [black on blue]{self.nome}[/]'
        conteudo += f'\nJogos favoritos:'
        for c in lista_de_jogos:
            conteudo += f'\n:video_game: [blue]{c}[/]'

        produto = Panel(f'{conteudo}', title=f'Jogador <{self.nick}>', width=40)

        print(produto)

j1 = Gamer('Naruto', 'detonator2025')
j1.add_favoritos('Mario Bros.')
j1.add_favoritos('Sonic')
j1.add_favoritos('God of war')
j1.add_favoritos('Fortnite')
j1.ficha()