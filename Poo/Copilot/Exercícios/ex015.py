class item_estoque:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

class alimento(item_estoque):

    def repor(self):
        if self.quantidade == 0:
            print(f'A {self.nome} tem {self.quantidade} em estoque e precisa repor')

    def retirar(self):
        if self.quantidade > 130:
            print(f'A {self.nome} tem {self.quantidade} em estoque e precisa retirar')

class bebidas(item_estoque):

    def repor(self):
        if self.quantidade == 0:
            print(f'A {self.nome} tem {self.quantidade} em estoque e precisa repor')

    def retirar(self):
        if self.quantidade > 130:
            print(f'A {self.nome} tem {self.quantidade} em estoque e precisa retirar')

class limpeza(item_estoque):

    def repor(self):
        if self.quantidade == 0:
            print(f'A {self.nome} tem {self.quantidade} em estoque e precisa repor')

    def retirar(self):
        if self.quantidade > 130:
            print(f'A {self.nome} tem {self.quantidade} em estoque e precisa retirar')

alimento('comida', 300).retirar()
bebidas('bebida', 0).repor()
