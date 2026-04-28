import datetime
maior = 0
menor = 0
for c in range(1, 8):
    idade = int(input('Em que ano a {} pessoa nasceu?  '.format(c)))
    if datetime.datetime.now().year - idade>= 18:
        maior += 1
    else:
        menor += 1
print('{} pessoas sao maior de idade'.format(maior))
print('{} pessoas sao menor de idade'.format(menor))