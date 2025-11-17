import time
def contador(i, f, p):
    print('Contador de {} até {} de {} em {}'.format(i, f, p, p))
    if p < 0:
        f -= 1
    elif p > 0:
        f += 1
    for c in range(i, f, p):
        print(c, end=' ')
        time.sleep(0.5)
    print()
print('-='*20)
contador(1, 11, 1)
print('-='*20)
contador(10, -1, -2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
print('FIM!')