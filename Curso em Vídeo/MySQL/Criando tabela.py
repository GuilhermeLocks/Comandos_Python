import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="")
cursor = con.cursor()
cursor.execute('use naruto')

cursor.execute("""
CREATE TABLE funcionarios (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cargo VARCHAR(100),
    salario FLOAT
)
""")

print("Tabela criada com sucesso!")