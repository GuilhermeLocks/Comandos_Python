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
    if linha_11 == 'x' and linha_33 == '9':
        linha_33 = 'o'
        jogadas_diponiveis.remove(9)
        jogo += 1
    if jogada_computador == 1:
        if linha_13 == '3':
            linha_13 = 'o'
            jogadas_diponiveis.remove(3)
            jogo += 1
        elif linha_13 == 'x' and linha_31 == '7':
            linha_31 = 'o'
            jogadas_diponiveis.remove(7)
            jogo += 1
