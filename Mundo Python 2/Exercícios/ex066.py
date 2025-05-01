total = cont = 0
while True:
    valor = input('Digite uma valor (999 para parar): ')
    if valor.isnumeric() == True:
        valor = int(valor)
        if valor == 999:
            break
        else:
            total += valor
            cont += 1
    else:
        print('Comando invalido, tente novamente.')
print('A soma dos {} valores foi {}!'.format(cont, total))