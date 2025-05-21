dicionario = {}
pessoas = []
continuar = ''
contador = 0
idade_total = 0
mulheres = list()
idade = 0
while continuar != 'N':

    while True:
        nome = input('Nome: ')
        if nome.isalpha() == True:
            dicionario['nome'] = nome
            contador += 1
            break
        else:
            print('ERRO! Por favor, digite apenas letras.')


    while True:
        dicionario['sexo'] = input('Sexo: [M/F]').upper()
        if dicionario['sexo'] == 'M' or dicionario['sexo'] == 'F':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')

    while True:
        idade = input('Idade: ')
        if idade.isnumeric() == True:
            idade = int(idade)
            dicionario['idade'] = idade
            idade_total += idade
            break
        else:
            print('ERRO! Por favor, digite apenas números.')


    while True:
        continuar = input('Quer continuar?').upper()
        if continuar == 'S' or continuar == 'N':
            break
        else:
            print('ERRO! Responda apenas S ou N.')

    pessoas.append(dicionario.copy())
    dicionario.clear()
print(pessoas)
print('-='*40)
print('A) Ao todo temos {} pessoas cadastradas.'.format(contador))
print('B) A média de idade é de {} anos'.format(idade_total/contador))
print('C) As mulheres cadastradas foram ', end = '')
for c in range(0, len(pessoas)):
    if pessoas[c]['sexo'] == 'F':
        print(pessoas[c]['nome'], end=' ')
print('\nd) Lista das pessoas que estão acima da média:')
for c in range(0, len(pessoas)):
    if pessoas[c]['idade'] > idade_total/contador:
        print(pessoas[c])
print()