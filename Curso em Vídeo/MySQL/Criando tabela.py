import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="")
cursor = con.cursor()

try:
    cursor.execute('use naruto')
    cursor.execute("""
    CREATE TABLE ninjas (
        id INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(30) not null,
        nascimento date,
        sexo enum ('M', 'F'),
        altura decimal (3,2),
        nacionalidade varchar (20) default 'Konaha',
        PRIMARY KEY(id)
    ) default charset = utf8
    """)
except:
    print('Erro ao criar tabela.')
else:
    print("Tabela criada com sucesso!")