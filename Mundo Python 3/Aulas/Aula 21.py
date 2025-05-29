#help(dict)
#print('-='*50)
#print(input.__doc__)
n = 1
def contador(i=0, f=20, p=2):
    '''
    utilizado para realizar uma contagem com números negativos e positivos
    e podendo alterar o passo
    :param i: utilizar i para o início do contador
    :param f: utilizar f para o fim do contador
    :param p: utilizar p para o passo do contador
    :return:
    '''
    if p > 0:
        f += 1
    elif p < 0:
        f -= 1
    for c in range(i, f, p):
        print(c, end=' ')
    n = 0
    print('n = ',n)
contador(10, 0, -1)
print()
contador(0, 10, 1)
print()
contador()
print()
help(contador)
print('n = ',n)
