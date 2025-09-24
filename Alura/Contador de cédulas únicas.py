while True:

    try:
        valor = int(input('Digite o valor do saque: '))
        if valor % 2:
            break

        else:

            print('Erro: O valor deve ser múltiplo de 2.')
    except:
        print('Erro: Valor invalido')
print('erro')
cedula_100 = 0
cedula_50 = 0
cedula_20 = 0
cedula_10 = 0
cedula_5 = 0
cedula_2 = 0

while True:
    print(valor)
    if valor >= 100:
        cedula_100 += 1
        valor -= 100
    if valor < 100:
        break

while True:
    if valor >= 50:
        cedula_50 += 1
        valor -= 50
    if valor < 50:
        break

while True:
    if valor >= 20:
        cedula_20 += 1
        valor -= 20
    if valor < 20:
        break

while True:
    if valor >= 10:
        cedula_10 += 1
        valor -= 10
    if valor < 10:
        break

while True:
    if valor >= 5:
        cedula_5 += 1
        valor -= 5
    if valor < 5:
        break

while True:
    if valor >= 2:
        cedula_2 += 1
        valor -= 2
    if valor < 2:
        break

print(f'O valor de {valor} de {cedula_100} cedulas de 100, {cedula_50} celulas de 50, {cedula_20} celulas de 20, {cedula_10} celulas de 10, {cedula_5} celulas de 5, {cedula_2} celulas de 2.')