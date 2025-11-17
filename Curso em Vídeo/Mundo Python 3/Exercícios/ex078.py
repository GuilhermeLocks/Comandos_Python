lista = []
posicao_maior = []
posicao_menor = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input('Digite um valor para a  Posição {}: '.format(c))))
    for c in lista:
        if c > maior:
            maior = c
        if menor == 0:
            menor = c
        if c < menor:
            menor = c
for p, c in enumerate(lista):
    if c == maior:
        posicao_maior.append(p)
    if c == menor:
        posicao_menor.append(p)
print('-='*20)
print('Você digitou os valores {}'.format(lista))
print('O maior valor digitado {} nas posições '.format(maior), end='')
for c in posicao_maior:
    print('{}... '.format(c), end='')
print(f'\nO menor valor digitado {menor} nas posições', end=' ')
for c in posicao_menor:
    print('{}... '.format(c), end='')