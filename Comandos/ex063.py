primeiro = 0
segundo = 1
print(primeiro, end=' ')
print(segundo, end=' ')
for c in range(0, 3):
    terceiro = primeiro + segundo
    print(terceiro, end=' ')
    quarto = terceiro + segundo
    print(quarto, end=' ')
    primeiro = terceiro + quarto
    segundo = quarto + primeiro
    print(primeiro, end=' ')
    print(segundo, end=' ')