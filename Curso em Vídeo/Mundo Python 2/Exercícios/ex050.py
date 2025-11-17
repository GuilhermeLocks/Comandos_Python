soma = 0
cont = 0
for c in range(0,6):
    valor = int(input('Digite uma valor: '))
    cont += 1
    if valor % 2 ==0:
        soma += valor
print('Você informou {} e a soma dos numeros pares é {}'.format(cont, soma))