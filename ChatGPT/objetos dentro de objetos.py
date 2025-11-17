class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade

class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def mostar_dados(self):
        print(f'Cliente: {self.nome}')
        print(f'Endereço: {self.endereco.rua}, {self.endereco.cidade}')

end = Endereco('Rua das Flores', 'Tubarão')
cli = Cliente('Guilherme', end)
cli.mostar_dados()