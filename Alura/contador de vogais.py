texto = str(input('Digite um texto: '))

vogais = ['a', 'e', 'i', 'o', 'u']
contador = 0

for c in texto:
    if c in vogais:
        contador += 1

print(f'O texto contém {contador} vogais')