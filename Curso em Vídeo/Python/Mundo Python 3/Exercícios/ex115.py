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


def cabeçalho(txt):
    print(Linha())
    print(txt.center(42))
    print(Linha())

def menu(lista):
    cabeçalho('Menu Principal')
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

def criaArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro ao criar o arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos.')
    finally:
        a.close()

def cadastrar(arquivo, nome='desconhecido', idade='0'):
    try:
        a = open(arquivo, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao abrir o arquivo.')


arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criaArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastras', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...Ate logo!')
        break
    else:
        print('\033[31m Digite uma opção válida!\033[m')
    sleep(2)