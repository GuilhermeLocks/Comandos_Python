class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_descomto(self):
        print(f'O produto {self.nome} tem o preço de R${self.preco} com 10% de desconto ficara R${self.preco * 0.90:.2f}')

class produto_digital(produto): pass
class produto_fisico(produto): pass

produto_digital('Nome Produto', 500).aplicar_descomto()
produto_fisico('Nome Produto', 200).aplicar_descomto()