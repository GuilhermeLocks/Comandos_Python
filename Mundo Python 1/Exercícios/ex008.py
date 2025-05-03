while True:
    n1 = input('Uma distância em metros: ')
    if n1.isnumeric() == True:
        n1 = float(n1)
        break
    else:
        print('Distância invalida, tente novamente.')
print('A medida em {} corresponde a'.format(n1))
print('{}Km'.format(n1/1000))
print('{}Hm'.format(n1/100))
print('{}dam'.format(n1/10))
print('{}dm'.format(int(n1*10)))
print('{}cm'.format(int(n1*100)))
print('{:.0f}mm'.format(n1*1000))