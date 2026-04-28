cont =0
total = 0
while True:
    numero = input('Digite um número [999 para parar]: ')
    if numero.isnumeric() == True:
        numero = int(numero)
        if numero == 999:
            break
        else:
            total += numero
            cont += 1
    else:
        print('Número invalido, tente novamente.')
        total += int(numero)
print('Você digitou {} e a soma entre eles foi {}.'.format(cont, total))

