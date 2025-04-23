while True:
    tabuada = input('Quer ver a tabuada de qual valor? ')
    print('-'*40)
    if tabuada < str(0):
        break
    if tabuada.isnumeric() == True:
        tabuada = int(tabuada)
        for c in range(1, 11):
            print('{} X {} = {}'.format(c, tabuada, tabuada*c))
        print('-'*40)
    else:
        print('Comando invalidado, tente novamente.')