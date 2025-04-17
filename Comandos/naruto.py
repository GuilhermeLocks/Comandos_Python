import time

numero = 2

while True:
    contador = 0
    for c in range(1, numero + 1):
        if numero % c == 0:
            contador += 1
    if contador == 2:
        print(numero)
    numero += 1



