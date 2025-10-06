class restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_placa = restaurante('Praça', 'Gourmet')
restaurante_pizza = restaurante('Pizza', 'Italiana')

restaurantes = [restaurante_placa, restaurante_pizza]

print(vars(restaurante_placa))
print()
print(dir(restaurante_placa))
print()
print(restaurante_placa)