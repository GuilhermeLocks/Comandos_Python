maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(c)))

    if menor == 0:
        menor = peso

    if maior < peso:
        maior = peso

    if  menor > peso:
        menor = peso

print(maior, menor)

