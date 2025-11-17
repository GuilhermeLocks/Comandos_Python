#while True:
#    primeiro = int(input('Primeiro segmento:'))
#    segundo = int(input('Segundo segmento: '))
#    terceiro = int(input('Terceiro segmento:'))
#    triangulo = 'nao'
#    if primeiro + segundo > terceiro and segundo + terceiro > primeiro and primeiro + terceiro > segundo:
#        triangulo = 'sim'
#    if triangulo == 'sim':
#        if primeiro == segundo and segundo == terceiro:
#            print('E um triangulo equilátero')
#        elif primeiro != segundo and segundo != terceiro and terceiro != primeiro:
#            print('E um triangulo escaleno')
#        else:
#            print('E um triangulo isósceles')
#        break
#    else:
#        print('Nao e um triangulo tente novamente.')
valor = 0
def classificar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            valor = 1
            return 'É um triângulo equilátero'
        elif a != b and b != c and c != a:
            return 'É um triângulo escaleno'
        else:
            return 'É um triângulo isósceles'
    else:
        return 'Não é um triângulo'


while True:
    a = int(input('Primeiro segmento: '))
    b = int(input('Segundo segmento: '))
    c = int(input('Terceiro segmento: '))

    resultado = classificar_triangulo(a, b, c)
    print(resultado)
    print(classificar_triangulo(a, b, c))

    if 'triângulo' in resultado:
        break

