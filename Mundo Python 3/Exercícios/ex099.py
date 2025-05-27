import random
import time
def maior(* num):
    maio = 0
    cont = 0
    print('Analizando os valores passados...')
    for c in num:
        print(c, end=' ')
        cont += 1
        time.sleep(0.5)
        if maio == 0:
            maio = c
        elif maio < c:
            maio = c
    print('foram informados {} valores ao todo.'.format(cont))
    time.sleep(0.5)
    print('O maior valor informado foi {}'.format(maio))


maior(random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20))
maior(random.randint(1, 20), random.randint(1, 20), random.randint(1, 20))
maior(random.randint(1, 20), random.randint(1, 20))