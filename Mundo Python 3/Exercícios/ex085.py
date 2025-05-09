lista_total = []
lista_par = []
lista_impar = []
for c in range(0, 7):
    while True:
        valor = input('Digite um valor: ')
        if valor.isnumeric() == True:
            valor = int(valor)
            break
        else:
            print('Valor invalido, tente novamente.')
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
lista_total.append(lista_par[:])
lista_total.append(lista_impar[:])
print(lista_total)