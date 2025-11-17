lista_abre = 0
lista_fecha = 0
expressao = input('Digite a expressão:')
for c in expressao:
    if c == '(':
        lista_abre += 1
    elif c == ')':
        lista_fecha += 1
if lista_abre == lista_fecha:
    print('Sua expressão está certa!')
else:
    print('Sua expressão está errada!')