    #calcula o imposto

def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor *0.3
    else:
        imposto = valor * 0.2
    return imposto

    #valor do produto

preco_produto1 = 1000

    #usa o calcu do imposto e atribui a uma variavel

imposto_produto1= calcular_imposto(preco_produto1)

    # aparece o valor do imposto


print(imposto_produto1)
