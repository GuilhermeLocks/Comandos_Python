class restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_placa = restaurante()
restaurante_placa.nome = 'Plaça'
restaurante_placa.categoria = 'Gourmet'

restaurante_pizza = restaurante()

restaurantes = [restaurante_placa, restaurante_pizza]

print(vars(restaurante_placa))
print()
print(dir(restaurante_placa))