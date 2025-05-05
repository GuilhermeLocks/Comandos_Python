while True:
    n1 = input('Informe a temperatura em °C: ')
    if n1.isnumeric() == True:
        n1 = float(n1)
        break
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F!'.format(n1, (n1*1.8)+32))