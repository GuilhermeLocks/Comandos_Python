from modelos.restaurante import Restaurante
from Alura.Sabor_Express.modelos.cardapio.prato import Prato
from Alura.Sabor_Express.modelos.cardapio.bebida import Bebida

restaurante_placa = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.00, 'Grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
restaurante_placa.adicionar_no_cardapio(bebida_suco)
restaurante_placa.adicionar_no_cardapio(prato_paozinho)


# restaurante_pizza = Restaurante('pizza', 'Italiana')
# restaurante_placa.receber_avaliacao('Gui', 5)
# restaurante_placa.receber_avaliacao('Gui', 2)
# restaurante_pizza.receber_avaliacao('Gui', 5)
# restaurante_pizza.receber_avaliacao('Gui', 4)
# restaurante_placa.alternar_estado()

def main():
    restaurante_placa.exibir_cardapio

if __name__ == '__main__':
    main()