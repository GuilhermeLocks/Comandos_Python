resultado = 0
while True:
    fator = input('Digite um número para calcular seu fatorial: ')
    if fator.isnumeric() == True:
        fator = int(fator)
    else:
        print('Número invalido, tente novamente')
    for c in range(fator - 1, 0, -1):
        fator *= c
    break
print(fator)