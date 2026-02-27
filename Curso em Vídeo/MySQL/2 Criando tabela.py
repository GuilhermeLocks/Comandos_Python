import mysql.connector
database = input('Digite o nome do bando de dados: ')
con = mysql.connector.connect(host="localhost", user="root", password="", database=database)
cursor = con.cursor()
# import sqlite3
# conexao = sqlite3.connect('''cadastro.db''''')
# cursor = conexao.cursor()

while True:
    comando = input('Digite pessoas ou cursos para criar a tabela:')
    if comando == 'pessoas' or comando == 'cursos':
        break
    else:
        print('Comando invalido tente novamente')

if comando == 'pessoas':
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
    except Exception as erro:
        print(f'Erro: {erro}.')
    else:
        print("Tabela criada com sucesso!")

if comando == 'cursos':
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
    except Exception as erro:
        print(f'Erro: {erro}.')
    else:
        print("Tabela criada com sucesso!")