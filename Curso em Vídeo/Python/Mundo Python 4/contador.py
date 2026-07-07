comeco = int(input('Começo: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

if comeco > fim:
    passo = -passo
    fim = fim-2

for c in range(comeco, fim+1, passo):
    print(c)