from random import randint
numero_aleatorio = randint(1, 100)
while True:
    try:
        numero_jogador = int(input(f'Tente adivinhar o número (1-100):'))
        if numero_jogador < 1 or numero_jogador > 100:
            print('Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.!')
        else:
            break
    except ValueError:
        print('Entrada inválida')
if numero_jogador == numero_aleatorio:
    print(f'Parabéns! Você acertou o número {numero_jogador}!')