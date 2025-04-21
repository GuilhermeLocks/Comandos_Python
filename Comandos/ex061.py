while True:
    valor = input('valor: ' )
    if valor.isnumeric() == True:
        valor = int(valor)
        break
    else:
        print('Valor invalido, tente novamente.')
while True:
    passo = input('passo: ')
    if passo.isnumeric() == True:
        passo = int(passo)
        break
    else:
        print('Passo invalido, tente novamente.')
print(valor, end=' -> ')
for c in range(1, 10):
    print(valor+(passo*c), end=' -> ')