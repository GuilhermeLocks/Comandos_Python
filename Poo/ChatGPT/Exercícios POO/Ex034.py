class Produto:
    taxa_imposto = 0.1  # 10%

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @classmethod
    def atualizar_imposto(cls, nova_taxa):
        cls.taxa_imposto = nova_taxa

Produto.atualizar_imposto(0.2)
print(Produto.taxa_imposto)
