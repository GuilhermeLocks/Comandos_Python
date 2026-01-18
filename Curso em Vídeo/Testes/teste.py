encomendas = input("Digite os números das encomendas separados por vírgula: ").split(',')
print(encomendas)
try:
    for encomenda in encomendas:
        print(int(encomenda))
except ValueError:
    print("Uma das entradas não é um número válido.")