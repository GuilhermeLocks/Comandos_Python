fibonacci = []
primeiro = 0
fibonacci.append(primeiro)
segundo = 1
fibonacci.append(segundo)
fim = int(input('fim: '))
for c in range(0, fim):
    terceiro = primeiro + segundo
    fibonacci.append(terceiro)
    quarto = terceiro + segundo
    fibonacci.append(quarto)
    primeiro = terceiro + quarto
    segundo = quarto + primeiro
    fibonacci.append(primeiro)
    fibonacci.append(segundo)
print(fibonacci[:fim])