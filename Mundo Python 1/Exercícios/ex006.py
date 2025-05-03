while True:
    n1 = input('Digite um numero: ')
    if n1.isnumeric() == True:
        n1 = int(n1)
        break
    else:
        print('Número invalido, tente novamente.')
print('O dobro de {} vale {}.'.format(n1, (n1*2)))
print('O triplo de {} vale {}. \nA rais quadra de {} é igual a  {}.'.format(n1, (n1*3), n1, (pow(n1, (1/2)))))

