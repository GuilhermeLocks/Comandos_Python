import random
numero = random.randint(1, 10)
tentativa = 0
while True:
    chute = int(input('Digite um numero: '))
    if chute == numero:
        tentativa += 1
        break
    elif chute > numero:
        tentativa += 1
        print('Tente um numero menor')
    elif chute < numero:
        tentativa += 1
        print('Tente um numero maior')

print(f'Voce acertou em {tentativa} tentativas')