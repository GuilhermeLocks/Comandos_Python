fim = int(input('fim: '))
fibonacci = []
primeiro = 0
if len(fibonacci) < fim:
    fibonacci.append(primeiro)
segundo = 1
if len(fibonacci) < fim:
    fibonacci.append(segundo)
for c in range(0, fim):
    terceiro = primeiro + segundo
    if len(fibonacci) < fim:
        fibonacci.append(terceiro)
    quarto = terceiro + segundo
    if len(fibonacci) < fim:
        fibonacci.append(quarto)
    primeiro = terceiro + quarto
    segundo = quarto + primeiro
    if len(fibonacci) < fim:
        fibonacci.append(primeiro)
    if len(fibonacci) < fim:
     fibonacci.append(segundo)
print(fibonacci)