n1 = float(input('Largura da parede:'))
n2 = float(input('Altura da parede:'))
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.1f}m².'.format(n1, n2, (n1*n2)))
print('Para pintar essa parede, você precisarà de {:.1f}L de tinta.'.format((n1*n2)/2))