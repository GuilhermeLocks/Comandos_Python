def somar(a, b):
    return a + b

try:
    numero_1 = int(input('Digie um numero: '))
    numero_2 = int(input('Digite outro numero: '))
    resultado = somar(numero_1, numero_2)
    print(f'A soma entre {numero_1} e {numero_2} deu {resultado}')

except ValueError:
    print('Erro: Digite apenas números válidos!')
