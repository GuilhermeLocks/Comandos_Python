import random
print("-="*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)
jogo_1 = ''
jogo_2 =''
cont = 0
result = ''
while True:
    valor_2 = random.randint(1, 2)
    while True:
        valor_1 = input('Diga uma valor: ')
        if valor_1.isnumeric() == True:
            valor_1 = int(valor_1)
            break
        else:
            print('Comando invalido, tente novamente')

    while True:
        escolha = input('Par ou ímpar? [P/I] ').upper()
        if escolha == 'P' or escolha == 'I':
            break
        else:
            print('Comando invalido, tente novamente.')
    print('-=' * 20)
    if valor_1 % 2 == 0:
        jogo_1 = 'par'
    else:
        jogo_1 ='ímpar'

    if valor_2 % 2 == 0:
        jogo_2 = 'par'
    else:
        jogo_2 ='ímpar'

    if jogo_1 == 'par' and jogo_2 == 'par':
        if escolha == 'P':
            print('Você ganhou')
            cont += 1
            result = 'par'
        else:
            result = 'ímpar'
            break

    if jogo_1 == 'par' and jogo_2 == 'ímpar':
        if escolha == 'P':
            result = 'par'
            break
        else:
            print('Você ganhei')
            cont += 1
            result = 'ímpar'

    if jogo_1 == 'ímpar' and jogo_2 == 'par':
        if escolha == 'P':
            result = 'par'
            break
        else:
            print('Você ganheu')
            cont += 1
            result = 'ímpar'

    if jogo_1 == 'ímpar' and jogo_2 == 'ímpar':
        if escolha == 'P':
            print('Você ganhou')
            cont += 1
            result = 'par'
        else:
            result = 'ímpar'
            break
    print('Você jogou {} e o computador {}. Total de {} DEU {}'.format(valor_1, valor_2, valor_1 + valor_2, result))
    print('-=' * 20)
print('Você perdeu')
print('Você jogou {} e o computador {}. Total de {} DEU {}'.format(valor_1, valor_2, valor_1+valor_2, result))
print('-=' * 20)
print('GAME OVER! Você ganhou {} vezes.'.format(cont))
