from rich import print
class Diario:
    def __init__(self, senha='nao tem'):
        self.senha = senha
        self.conteudo = []

    def escrever(self, conteudo):
        self.conteudo.append(conteudo)

    def ler(self, senha):
        
        if self.senha == senha or self.senha == 'nao tem':
            print('[green]Diário LIBERADO!')
            for c in self.conteudo:
                print(f'- {c}')
        else:
            print('[red]Senha INCORRETA!')

d= Diario()

d.escrever('Primeira mensagem')
d.escrever('Você é uma pessoa simpática')
d.escrever('Você gosta de Python')

d.ler('senha')