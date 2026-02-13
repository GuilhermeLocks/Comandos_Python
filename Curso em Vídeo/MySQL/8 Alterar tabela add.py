import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='', database='cadastro')
cursor = con.cursor()

while True:
    try:
        comando = int(input('''1 Adiciona coluna profissão
2 Adicinada coluna profissão depois de nome
3 Adicinada coluna profissão em primeiro lugar
4 Modificada coluna profissão
5 Renomeada coluna profissão para prof
6 Renomeada tabela pessoas para pessoa
7 Adicionado idcurso em primeiro lugar
8 Alterado idcurso para chave primaria
9 Deletar coluna profissão
Digite um numero entre 1 a 9:'''))
    except:
        print('Comando invalido tentenovamente!')
    if comando >= 1 and comando <= 9:
        break
    else:
        print('Comando invalido tente novamente')

if comando == 1:
    try:
        cursor.execute('''alter table pessoas
                       add column profissao varchar(10);''')
        print('Coluna profissão adicinada com sucesso!')

    except Exception as erro:
        print(f'Erro: {erro}')
if comando == 2:
    try:
        cursor.execute('''alter table pessoas
                       add column profissao varchar(10) after nome;''')
        print('Coluna profissão adicinada depois de nome com sucesso!')

    except Exception as erro:
        print(f'Erro: {erro}')
if comando == 3:
    try:
        cursor.execute('''alter table pessoas
                       add column profissao varchar(10) first;''')
        print('Coluna profissão adicinada em primeiro lugar com sucesso!')

    except Exception as erro:
        print(f'Erro: {erro}')
if comando == 4:
    try:
        cursor.execute('''alter table pessoas
                       modify column profissao varchar(20) not null;''')
        print('Coluna profissão modificada com sucesso!')

    except Exception as erro:
        print(f'Erro: {erro}')
if comando == 5:
    try:
        cursor.execute('''alter table ninjas
                       change column profissao prof varchar(20);''')
        print('Coluna profissão renomeada para prof com sucesso!')

    except Exception as erro:
        print(f'Erro: {erro}')
if comando == 6:
    try:
        cursor.execute('''alter table pessoas
                       rename to pessoa;''')
        print('Tabela pessoas renomeada para pessoas com sucesso!')

    except Exception as erro:
        print(f'Erro: {erro}')

if comando == 7:
    try:
        cursor.execute('''alter table cursos
                       add column idcurso int first;''')
        print('Adicionado idcurso em primeiro lugar com sucesso!')

    except Exception as erro:
        print(f'Erro: {erro}')

if comando == 8:
    try:
        cursor.execute('''alter table cursos
                       add primary key(idcurso);''')
        print('Alterado idcurso para chave primaria com sucesso!')

    except Exception as erro:
        print(f'Erro: {erro}')

if comando == 9:
    try:
        cursor.execute('''alter table pessoas
                       drop column prof;''')
        print('Coluna profissão deletada com sucesso!')

    except Exception as erro:
        print(f'Erro: [{erro}')