import os

restaurantes = [{'nome': 'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome': 'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome': 'Cantina', 'categoria':'Italiana', 'ativo':False}]

def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    eibir_subtitulo('Finalizando o app!')

def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print(f'𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n')

def exibir_opcaoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterna estado do restaurante')
    print('4. Sair\n')

def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante

        Outputs:
        - Exibe mensagem indicando o sucesso da operação
        '''
    eibir_subtitulo('Alternando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterna o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            if restaurante['ativo'] == True:
                print(f'O restaurante {nome_restaurante} foi ativado com sucesso')
            else:
                print(f'O restaurante {nome_restaurante} foi desativado com sucesso')

    if restaurante_encontrado == False:
        print('O restaurante não foi encontrado ')


    voltar_ao_menu_principal()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário

        Outputs:
        - Executa a opção escolhida pelo usuário
        '''
    while True:
        try:
            opcao = int(input('Escolha uma opção: '))

            if opcao == 1:
                cadastrar_novo_restaurante()
            elif opcao == 2:
                listar_restaurantes()
            elif opcao == 3:
                alternar_estado_restaurante()
            elif opcao == 4:
                finalizar_app()
                break
            else:
                opcao_invalida()
        except:
            opcao_invalida()

def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal

        Outputs:
        - Retorna ao menu principal
        '''
    print('Opção invalida, tentenovamente.')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal

        Outputs:
        - Retorna ao menu principal
        '''
    input('\nDigite uma tecla para voltar ao menu')
    main()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante

    Input:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante na lista de restaurantes
    '''

    eibir_subtitulo('Cadastrado de novos restaurantes!')

    nome_do_restaurante = input('Nome do restaurante: ')
    categoria = input(f'Digite o noma de categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado.')

    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista

        Outputs:
        - Exibe a lista de restaurantes na tela
        '''
    eibir_subtitulo('Listando os restaurantes:')
    print(f'{'nome do restaurante'.ljust(22)} | {'categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']

        if ativo == True:
            print(f'- {nome_restaurante:<20} | {categoria:<20} | ativado')
        else:
            print(f'- {nome_restaurante:<20} | {categoria:<20} | desativado')

    voltar_ao_menu_principal()

def eibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela

        Inputs:
        - texto: str - O texto do subtítulo
        '''
    os.system('cls')
    linha = '*'*len(texto)
    print(linha)
    print(f'{texto}')
    print(linha)
    print()

def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcaoes()
    escolher_opcao()
    # print(cadastrar_novo_restaurante.__doc__)

if __name__ == '__main__':
    main()