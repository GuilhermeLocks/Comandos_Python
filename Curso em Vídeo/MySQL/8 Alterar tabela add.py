import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='', database='naruto')
cursor = con.cursor()

while True:
    try:
        comando = int(input('Digite um numero entre 1 a 8:'))
    except:
        print('Comando invalido tentenovamente!')
    if comando >= 1 and comando <= 8:
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
        print('Coluna profissão adicinada com sucesso!')

    except Exception as erro:
        print(f'Erro: {erro}')
if comando == 3:
    try:
        cursor.execute('''alter table pessoas
                       add column profissao varchar(10) first;''')
        print('Coluna profissão adicinada com sucesso!')

    except Exception as erro:
        print(f'Erro: {erro}')
if comando == 4:
    try:
        cursor.execute('''alter table pessoas
                       modify column profissao varchar(20) not null;''')
        print('Coluna profissão adicinada com sucesso!')

    except Exception as erro:
        print(f'Erro: {erro}')
if comando == 5:
    try:
        cursor.execute('''alter table ninjas
                       change column profissao prof varchar(20);''')
        print('Coluna profissão adicinada com sucesso!')

    except Exception as erro:
        print(f'Erro: {erro}')
if comando == 6:
    try:
        cursor.execute('''alter table pessoas
                       rename to pessoa;''')
        print('Coluna profissão adicinada com sucesso!')

    except Exception as erro:
        print(f'Erro: {erro}')

if comando == 7:
    try:
        cursor.execute('''alter table cursos
                       add column idcurso int first;''')
        print('Coluna profissão adicinada com sucesso!')

    except Exception as erro:
        print(f'Erro: {erro}')

if comando == 8:
    try:
        cursor.execute('''alter table cursos
                       add primary key(idcurso);''')
        print('Coluna profissão adicinada com sucesso!')

    except Exception as erro:
        print(f'Erro: {erro}')