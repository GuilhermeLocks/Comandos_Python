import random
numero1 = random.randint(0, 10)
contador = 0
while True:
    print(numero1)
    numero2 = input(('Digite um valor:'))
    if numero2.isnumeric() == True:
        numero2 = int(numero2)
        contador += 1
        if numero2 == numero1:
            print(numero1, numero2, contador)
            break
    else:
        print('Tente novamente')
        contador += 1