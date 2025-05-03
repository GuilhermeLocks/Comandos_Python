while True:
    n = input('Digite um numero: ')
    if n.isnumeric() == True:
        n = int(n)
        break
    else:
        print('Número invalido, tente novamente.')
print('Analizando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))
