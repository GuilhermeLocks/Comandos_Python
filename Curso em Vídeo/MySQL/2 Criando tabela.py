import mysql.connector
database = 'cadastro'
con = mysql.connector.connect(host="localhost", user="root", password="")
cursor = con.cursor()

try:
    cursor.execute(f'use {database}')
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
    print(f'\nUSE {database}')
    print("""\nCREATE TABLE if not exists pessoas (
id INT NOT NULL AUTO_INCREMENT,
nome VARCHAR(30) not null unique,
nascimento date,
sexo enum ('M', 'F'),
altura decimal (3,2),
nacionalidade varchar (20) default 'Brasil',
PRIMARY KEY(id)
) default charset = utf8
    """)
    print("Tabela criada com sucesso!")


try:
    cursor.execute(f'use {database}')
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
    print(f'\nUSE {database}')
    print("""
CREATE TABLE if not exists cursos (
nome VARCHAR(30) not null unique,
descricao text,
carga int unsigned,
totaulas int,
ano year default '2016'
) default charset = utf8
    """)
    print("Tabela criada com sucesso!")