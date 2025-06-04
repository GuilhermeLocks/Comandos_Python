from utilidades.ex108_moeda import ex108_moeda

p = float(input('Digite o preço: R$'))
print('A metade de R${:.2f} é R${}'.format(p, ex108_moeda.metade(p)))
print('O dobro de R${:.2f} é R${}'.format(p, ex108_moeda.dobro(p)))
print('Aumentando 10%, temos R${}'.format(ex108_moeda.aumentar(p)))
print('Reduzindo 13%, temos R${}'.format(ex108_moeda.reduzir(p)))
