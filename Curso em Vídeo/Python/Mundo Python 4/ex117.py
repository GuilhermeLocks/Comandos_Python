from rich.panel import Panel
from rich import print
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        produto = Panel(f'{self.nome:^30}\n{'-'*30}\n{self.preco:.^30,.2f}', title=' Produto', width=34, height=5)
        print(produto)

p1 = Produto('iPhone 17 Pro Max', 25_000.85)
p2 = Produto('Notebook Gamer', 8_000)

p1.etiqueta()
p2.etiqueta()
