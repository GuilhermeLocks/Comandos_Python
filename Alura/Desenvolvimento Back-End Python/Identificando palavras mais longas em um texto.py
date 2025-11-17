texto = str(input('Digite um texto:'))
texto = texto.split()
contador = 0
lista = []
for c in texto:
    if len(c) > 10:
        contador += 1
        lista.append(c)
if contador > 0:
    print('Palavras longas encontradas:', end= ' ')
    for c in lista:
        if c != lista[(len(lista))-1]:
            print(c, end=', ')
        else:
            print(c, end='.')
else:
    print('Nenhuma palavra longa foi encontrada no texto.')

