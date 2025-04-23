primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print(primeiro,' ->', end = " ")
for c in range(1, 10):
    print(primeiro + (razao * c), '->', end = " ")
print('ACABOU!!!')