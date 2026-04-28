print('='*30)
print('          BANCO CEV           ')
print('='*30)

#variaveis das notas

nota_50 = nota_20 = nota_10 = nota_1 = 0

#recebe e verifica o valor

while True:
    valor = input('Que valor você quer sacar? R$')
    if valor.isnumeric() == True:
        valor = int(valor)
        break
    else:
        print('Comando invalido, tente novamente.')

#calcula a quantidade de notas

while valor != 0:
    if valor >= 50:
        valor -= 50
        nota_50 += 1
    elif valor >= 20:
        valor -= 20
        nota_20 += 1
    elif valor >= 10:
        valor -= 10
        nota_10 += 1
    elif valor >= 1:
        valor -= 1
        nota_1 += 1
print('='*30)

#aparece a quantidade de notas

if nota_50 > 0:
    print('O total de {} notas de R$50'.format(nota_50))
if nota_20 > 0:
    print('O total de {} notas de R$20'.format(nota_20))
if nota_10 > 0:
    print('O total de {} notas de R$10'.format(nota_10))
if nota_1 > 0:
    print('O total de {} notas de R$1'.format(nota_1))
