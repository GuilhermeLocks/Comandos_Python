import random
import time
lista = []
print('-'*50)
print(' '*15, 'JOGA NA MEGA SENA')
print('-'*50)
while True:
    roda = input('Quantos jogos você quer que eu sorte: ')
    if roda.isnumeric() == True:
        roda = int(roda)
        break
    else:
        print('Comando invalido, tente novamente.')


for c in range(1, roda+2):
    while len(lista) != roda:
        valor = random.randint(1, 60)
        if valor not in lista:
            lista.append(valor)
    time.sleep(1)
    lista.sort()
    print('Jogo {}: {}'.format(c, lista))
    lista.clear()