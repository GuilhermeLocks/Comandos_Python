tabuada = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} X {:2} = {:2}'.format(tabuada, c, tabuada*c))