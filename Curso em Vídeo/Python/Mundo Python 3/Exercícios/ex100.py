import random
import time
numero = [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)]


def lista(* num):
    print('Soteando os valores da lista:', end=' ')
    for c in numero:
        time.sleep(0.5)
        print(c, end=' ')
    time.sleep(0.5)
    print('PRONTO!')

def pares(* num):
    pares = 0
    print('Lista de numeros pares:', end=' ')
    for c in numero:
        if c % 2 == 0 and c != 0:
            pares += c
            time.sleep(0.5)
            print(c, end=' ')
    time.sleep(0.5)
    print('PRONTO!')
    time.sleep(0.5)
    print('A soma dos pares da {} PRONTO!'.format(pares))

lista(numero)
time.sleep(0.5)
pares(numero)
