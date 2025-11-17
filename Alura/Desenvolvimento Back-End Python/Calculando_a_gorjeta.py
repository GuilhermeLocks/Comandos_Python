valor = float(input('Digite o valor da conta: '))
gorjeta = int(input('Digite o porcetagem da gorjeta: '))
print(f'Valor da gorjeta: R$ {((valor/100)*gorjeta):.2f}')
print(f'Total a pagar: R$ {(valor + ((valor/100)*gorjeta)):.2f}')