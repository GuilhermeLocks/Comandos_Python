import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="")
cursor = con.cursor()

try:
    cursor.execute('use naruto')
    cursor.execute("""
    CREATE TABLE ninjas (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(30),
        nascimento date,
        sexo enum ('M', 'F'),
        altura decimal (3,2),
        nacionalidade varchar (30) default 'Konaha'
    )
    """)
except:
    print('erro')
else:
    print("Tabela criada com sucesso!")