restaurantes = []

def exibir_opcaoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    print('Finalizando o app!')

def exibir_nome_do_programa():
    print('''𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n''')

def cadastrar_novo_restaurante():
    print('Cadastrado de novos restaurantes!')
    nome_restaurante = input('Nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado.')
    print(restaurantes)
    print()

def escolher_opcao():
    while True:
        exibir_opcaoes()
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            cadastrar_novo_restaurante()
        elif opcao == '2':
            print('Listar restaurante')
        elif opcao == '3':
            print('Ativar restaurante')
        elif opcao == '4':
            finalizar_app()
            break
        else:
            print('Opçãa invalida, tente novamente.')

def main():
    exibir_nome_do_programa()
    escolher_opcao()

if __name__ == '__main__':
    main()