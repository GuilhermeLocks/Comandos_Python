soma = 0
contador = 0

for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c
        contador += 1

print('A soma de todos os {} valores solicitados é de {}'. format(contador, soma))