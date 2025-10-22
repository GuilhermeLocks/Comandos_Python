from modelos.restaurante import Restaurante

restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_mexicano.receber_avaliacao('Gui', 10)

def main():
    Restaurante.listar_restauramtes()

if __name__ == '__main__':
    main()