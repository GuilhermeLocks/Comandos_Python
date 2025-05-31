def numero_flutuante(a):
    cont = 0
    cont_ponto = 0
    for c in a:
        print(c)
        if c.isnumeric() == True:
            cont += 1
        if c == '.':
            cont += 1
            cont_ponto += 1

    print(len(a))
    if len(a) == cont and cont_ponto == 1:
        return 1
    else:
        print('ERRO')
        print(len(a), cont, cont_ponto)
        return 0
def numero_inteiro(a):
    if a.isnumeric() == True:
        return 1
    else:
        print('ERRO!')
        return  0
def palavra(a):
    if a.isalpha() == True:
        return 1
    else:
        print('ERRO!')
        return  0

verificador = 0
while verificador == 0:
    verificador = numero_inteiro(input('Digite um número inteiro: '))

verificador = 0
while verificador == 0:
    verificador = palavra(input('Digite uma palavra: '))

verificador = 0
while verificador == 0:
    verificador = numero_flutuante(input('Digite um numero com ponto: '))

