from datetime import date

class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class perecivel(produto):
    def __init__(self, nome, preco, validade):
        super().__init__(nome, preco)
        self.validade = validade

    def esta_vencido(self):
        if self.validade < date.today().day:
            print(f'Ainda esta dento da validade e falta {date.today().day - self.validade} para vencer.')
        else:
            print(f'Ja esta vencido ja venceu ha {self.validade - date.today().day} dias.')

perecivel('arroz', 25, 19).esta_vencido()
perecivel('feijão', 25, 25).esta_vencido()

