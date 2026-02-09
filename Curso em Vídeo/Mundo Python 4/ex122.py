from django.forms.widgets import Input
from rich.panel import Panel
from rich import print
class televisao:
    def __init__(self):

        print('')
        produto = Panel(f'[red]A TV está desligada', title=f'[ TV ]', width=30, height=3)
        print(produto)

        self.comando = input('< CH1 >   - VOL2 + ')

        if self.comando == '@':
            while True:
                print('')
                produto = Panel(f'CANAL  = [yellow]1[/] 2 3 4 5'
                                f'\nVOLUME = [green]1[/] 2 3 4 5', title=f'[ TV ]', width=30, height=4)
                print(produto)
                self.comando = input('< CH1 >   - VOL2 + ')

                if self.comando == '@':
                    break

        print('')
        produto = Panel(f'[red]A TV está desligada', title=f'[ TV ]', width=30, height=3)
        print(produto)

t1 = televisao()