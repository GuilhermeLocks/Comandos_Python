import random
import time


def lista(* num):
    print('Soteando os valores da lista:', end=' ')
    for c in num:
        time.sleep(0.5)
        print(c, end=' ')
    time.sleep(0.5)
    print('PRONTO!')


lista(random.randint(0, 20), random.randint(0, 20), random.randint(0, 20), random.randint(0, 20), random.randint(0, 20))
