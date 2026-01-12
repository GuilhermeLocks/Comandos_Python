print('''𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n''')
print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')

while True:
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        print('Cadastrar restaurante')
        break
    elif opcao == '2':
        print('Listar restaurante')
        break
    elif opcao == '3':
        print('Ativar restaurante')
        break
    elif opcao == '4':
        print('Sair')
        break
    else:
        print('Opção invalida, tente novamente!')

print(f'Voçe escolheu a opção {opcao}')