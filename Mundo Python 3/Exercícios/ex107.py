import ex107_moeda

p = float(input('Digite o preço: R$'))
print('A metade de {} é {}'.format(p, ex107_moeda.metade(p)))
print('O dobro de {} é {}'.format(p, ex107_moeda.dobro(p)))
print('Aumentando 10%, temos {}'.format(ex107_moeda.aumentar(p)))
print('Reduzindo 13%, temos {}'.format(ex107_moeda.reduzir(p)))
