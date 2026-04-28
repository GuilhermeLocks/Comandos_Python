situacao = {}
situacao['nome'] = input('Nome: ')
situacao['Média'] = int(input('Média de {}:'.format(situacao['nome'])))
print('-='*40)
for c in situacao:
    print('{} é igual a {}'.format(c, situacao[c]))
if situacao['Média'] >= 7:
    print('situação e iqual a aprovado')
elif 5 <= situacao['Média'] < 7:
    print('situação e igual a recuperação')
else:
    print('situação e igual a reprovado')