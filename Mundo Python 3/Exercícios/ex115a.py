print('-'*40)
print('             MENU PRINCIPAL')
print('-'*40)
print('1 - Ver pessoas cadastradas')
print('2 - Cadastrar nova Pessoa')
print('3 - Sair do Sistema')
print('-'*40)
while True:
    try:
        opcao = int(input('Sua Opção: '))
        if opcao >= 1 and opcao <=3:
            break
        else:
            print('ERRO! Digite uma opçãp valida!')
    except:
        print('ERRO: por favor digite um número inteiro válido.')