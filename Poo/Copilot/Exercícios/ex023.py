class pagamento:
    def __init__(self, valor):
        self.valor = valor

class cartao(pagamento):
    def __init__(self, valor):
        super().__init__(valor)

    def processar(self):
        print(f'O valor R${self.valor} parcelado em 10 vezes ficara R${(self.valor/10):.2f} por mes')

class boleto(pagamento):
    def __init__(self, valor):
        super().__init__(valor)

    def processar(self):
        print(f'O valor R${self.valor} no boleot fica R${self.valor}')

cartao(100).processar()
boleto(100).processar()