from rich import print

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampa = False

    def destampar(self):
        self.tampa = True

    def tampar(self):
        self.tampa = False

    def escrever(self, text):
        if self.tampa == True:
            if self.cor == 'azul':
                print(f'[blue]{text}', end='')
            if self.cor == 'vermelho':
                print(f'[red]{text}', end='')
            if self.cor == 'verde':
                print(f'[green]{text}', end='')
        else:
            if self.cor == 'azul':
                print(f'A [blue]canete[/] está tampada!', end='')
            if self.cor == 'vermelho':
                print(f'A [red]canete[/] está tampada!', end='')
            if self.cor == 'verde':
                print(f'A [green]canete[/] está tampada!', end='')

    def quebrar_linha(self, num):
        for c in range(0, num):
            print('')

c1 = Caneta('azul')
c2 = Caneta('vermelho')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()

c3.tampar()

c1.escrever('Olá, tudo bem?')
c1.quebrar_linha(2)
c2.escrever('Olá, tudo bem?')
c2.quebrar_linha(2)
c3.escrever('Olá, tudo bem?')
c3.quebrar_linha(2)