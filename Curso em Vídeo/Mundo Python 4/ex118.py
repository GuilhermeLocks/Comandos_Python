from rich.panel import Panel
from rich import print
class Chusrrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def analizar(self):
        produto = Panel(f'Analizando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]'
                        f'\nCada participante comerá 0.4Kg e cada Kg custa R$82.40'
                        f'\nRecomento comprar [blue]{self.quant*0.4:.3f}Kg[/] de carne'
                        f'\nO custo total será de [green]R${(self.quant*0.4)*82.40:.2f}[/]'
                        f'\nCada pessoa pagará [yellow]R${((self.quant*0.4)*82.40)/self.quant}[/] para participar.', title=self.titulo, width=70, height=7)
        print(produto)

c1 = Chusrrasco('Churras dos Amigos', 15)
c1.analizar()