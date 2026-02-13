import mysql.connector
database = input('Digite o nome do bando de dados: ')
con = mysql.connector.connect(host="localhost", user="root", password="", database=database)
cursor = con.cursor()

while True:
    comando = input('Digite um numero entre 1 a 2:')
    if comando == '1' or comando == '2':
        break
    else:
        print('Comando invalido tente novamente')

if comando == '1':
    try:
        cursor.execute("""
        CREATE TABLE if not exists pessoas (
            id INT NOT NULL AUTO_INCREMENT,
            nome VARCHAR(30) not null unique,
            nascimento date,
            sexo enum ('M', 'F'),
            altura decimal (3,2),
            nacionalidade varchar (20) default 'Brasil',
            PRIMARY KEY(id)
        ) default charset = utf8
        """)
    except:
        print('Erro ao criar tabela.')
    else:
        print("Tabela criada com sucesso!")

if comando == '2':
    try:
        cursor.execute("""
        CREATE TABLE if not exists cursos (
            nome VARCHAR(30) not null unique,
            descricao text,
            carga int unsigned,
            totaulas int,
            ano year default '2016'
        ) default charset = utf8
        """)
    except:
        print('Erro ao criar tabela.')
    else:
        print("Tabela criada com sucesso!")