from time import sleep
def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferio não digitar esse número.\033[m')
            return 0
        else:
            return n


def Linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(Linha())
    print(txt.center(42))
    print(Linha())

def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(Linha())
    opc = LeiaInt('\033[32mSua opção: \033[m')
    return opc


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True




arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArguivo(arq)
while True:
    respota = menu(['Ver pessoas cadastras', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif respota == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif respota == 3:
        cabeçalho('Saindo do sistema...Ate logo!')
        break
    else:
        print('\033[31m Digite uma opção válida!\033[m')
    sleep(2)