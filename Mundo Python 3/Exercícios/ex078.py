lista = []
posicao_maior = []
posicao_menor = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
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

print('O maior valor e {}!'.format(maior))
print(f'E sua posição na lista e {posicao_maior}')
print(f'O menor valor é {menor}!')
print('E sua posição na lista é {}!'.format(posicao_menor))