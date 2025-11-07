from modelos.restaurante import Restaurante
from Alura.Sabor_Express.modelos.cardapio.bebida import Bebida
from Alura.Sabor_Express.modelos.cardapio.prato import Prato

restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
bebido_suco = Bebida('Suco de melancia', 5.0, 'grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')

def main():
    print(bebido_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()