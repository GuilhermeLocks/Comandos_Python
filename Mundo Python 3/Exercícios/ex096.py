print('   Controle de terrenos')
print('-'*26)
def area(largura, comprimento):
    print('A área de um terreno {}x{} é de {}'.format(largura, comprimento, largura*comprimento))
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)