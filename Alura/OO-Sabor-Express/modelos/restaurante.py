class Restaurante:
    restarantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restarantes.append(self)

    def __str__(self):
        return f'{self.nome} / {self.categoria}'

    @classmethod
    def listar_restauramtes(cls):
        print(f'{'nome '.ljust(20)}{'/categoria '.ljust(20)}{'/status'.ljust(20)}')
        for restaurante in cls.restarantes:
            print(f'{restaurante.nome.ljust(20)}/{restaurante.categoria.ljust(20)}/{restaurante.ativo.ljust(20)}')

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'falso'

    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_placa = Restaurante('praça', 'Gourmet')
restaurante_pizza = Restaurante('pizza', 'Italiana')
restaurante_placa._ativo = True

restaurantes = [restaurante_placa, restaurante_pizza]

print(vars(restaurante_placa))
print()
print(dir(restaurante_placa))
print()
print(restaurante_placa)
print()
for c in restaurantes:
    print(c)
print()
Restaurante.listar_restauramtes()

restaurante_pizza.alternar_estado()

print()