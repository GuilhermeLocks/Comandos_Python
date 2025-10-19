from modelos.restaurante import Restaurante

restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')

def main():
    Restaurante.listar_restauramtes()

if __name__ == '__main__':
    main()