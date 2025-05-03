while True:
    n1 = input('Largura da parede: ')
    if n1.isnumeric() == True:
        n1 = float(n1)
        break
    else:
        print('Largura da parede, invalida tente novamente.')
while True:
    n2 = input('Altura da parede: ')
    if n2.isnumeric() == True:
        n2 = float(n2)
        break
    else:
        print('Altura da parede, invalida tente novamente.')
print('Sua parede tem a dimensão de {} x {} e sua área é de {:.1f}m².'.format(n1, n2, (n1*n2)))
print('Para pintar essa parede, você precisarà de {:.1f}L de tinta.'.format((n1*n2)/2))