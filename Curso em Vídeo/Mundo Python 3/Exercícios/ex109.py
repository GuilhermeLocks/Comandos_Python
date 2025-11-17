from utilidades.ex109_moeda import ex109_moeda

p = float(input('Digite o preço: R$'))
print('A metade de R${} é R${}'.format(ex109_moeda.formatar(p, True), ex109_moeda.metade(p, True)))
print('O dobro de R${} é R${}'.format(ex109_moeda.formatar(p, True), ex109_moeda.dobro(p, True)))
print('Aumentando 10%, temos R${}'.format(ex109_moeda.aumentar(p, True, 10)))
print('Reduzindo 13%, temos R${}'.format(ex109_moeda.reduzir(p, True, 13)))
