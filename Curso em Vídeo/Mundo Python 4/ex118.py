from rich.panel import Panel
from rich import print
class Chusrrasco:

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
        self.preco_kg = 82.40
        self.consumo_padrao = 0.4

    def quantidade_de_carne(self) -> float:
        return self.quant * self.consumo_padrao

    def custo_total(self):
        return self.quantidade_de_carne() * self.preco_kg

    def custo_individual(self):
        return self.custo_total() / self.quant

    def analizar(self):
        produto = Panel(f'Analizando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]'
                        f'\nCada participante comerá 0.4Kg e cada Kg custa R$82.40'
                        f'\nRecomento comprar [blue]{self.quantidade_de_carne()}Kg[/] de carne'
                        f'\nO custo total será de [green]R${self.custo_total():.2f}[/]'
                        f'\nCada pessoa pagará [yellow]R${self.custo_individual()}[/] para participar.', title=self.titulo, width=70, height=7)
        print(produto)

c1 = Chusrrasco('Churras dos Amigos', 15)
c1.analizar()