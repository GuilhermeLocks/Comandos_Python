class Restaurante:
    restarantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restarantes.append(self)

    def __str__(self):
        return f'{self.nome} / {self.categoria}'

    def listar_restauramtes():
        print(f'{'nome '.ljust(10)}{'/categoria '.ljust(15)}{'/status'.ljust(20)}')
        for restaurante in Restaurante.restarantes:
            print(f'{restaurante.nome.ljust(10)}/{restaurante.categoria.ljust(15)}/{restaurante.ativo.ljust(20)}')

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'falso'

restaurante_placa = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza', 'Italiana')

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



print()
Restaurante.listar_restauramtes()