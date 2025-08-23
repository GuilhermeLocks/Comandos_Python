class Produto:
    def __init__(self, nome):
        self.nome = nome
        self.avaliacoes = []

    def avaliar(self, nota):
        self.avaliacoes.append(nota)

    def media_avaliacoes(self):
        for c in self.avaliacoes:
            print(c)
        print(f'Media das avaliações: {sum(self.avaliacoes) / len(self.avaliacoes)}')

class ProdutoDigital(Produto): pass
class ProdutoFisico(Produto): pass

p = Produto('produto')
p.avaliar(100)
p.avaliar(200)
p.media_avaliacoes()