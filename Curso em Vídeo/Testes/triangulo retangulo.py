while True:
    try:
        triangulo_parte = int(input('Digite algo: '))
        break
    except:
        print('Valor invalido')

for c in range(1,triangulo_parte+1):
    print(c * '*')