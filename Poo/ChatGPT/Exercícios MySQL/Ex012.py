import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = con.cursor()

# Seleciona o banco de dados
cursor.execute("CREATE DATABASE IF NOT EXISTS empresa")
cursor.execute("USE empresa")

# Cria a tabela se ainda não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS departamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    localizacao VARCHAR(100)
)
""")

# Insere os dados
sql = "INSERT INTO departamentos (nome, localizacao) VALUES (%s, %s)"
valores = [
    ("Financeiro", "São Paulo"),
    ("RH", "Rio de Janeiro"),
    ("TI", "Curitiba")
]

cursor.executemany(sql, valores)
con.commit()

print("Departamentos inseridos com sucesso!")

# Mostra os dados inseridos
cursor.execute("SELECT * FROM departamentos")
for linha in cursor.fetchall():
    print(linha)

cursor.close()
con.close()
