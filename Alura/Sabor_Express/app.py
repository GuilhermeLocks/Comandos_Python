from modelos.restaurante import Restaurante

restaurante_placa = Restaurante('praça', 'Gourmet')
restaurante_pizza = Restaurante('pizza', 'Italiana')
restaurante_placa.receber_avaliacao('Gui', 5)
restaurante_placa.receber_avaliacao('Gui', 2)
# restaurante_pizza.receber_avaliacao('Gui', 5)
# restaurante_pizza.receber_avaliacao('Gui', 4)
restaurante_placa.alternar_estado()

def main():
    Restaurante.listar_restauramtes()

if __name__ == '__main__':
    main()