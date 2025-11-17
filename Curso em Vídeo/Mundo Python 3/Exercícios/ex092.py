from datetime import datetime
trabalho = {}
trabalho['nome']= str(input('nome: '))
trabalho['ano']= int(input('ano de nascimento: '))
trabalho['idade'] = datetime.now().year - trabalho['ano']
trabalho['carteira'] = int(input('carteira de trabalho (0 não tem):' ))
if trabalho['carteira'] != 0:
    trabalho['contratacao'] = int(input('ano de contratação: '))
    trabalho['salario'] = int(input('salario: R$'))
    trabalho['aposentario'] = (trabalho['contratacao'] + 35) - trabalho['ano']
print('-='*40)
for c in trabalho:
    print('{} tem o valor {}'.format(c, trabalho[c]))