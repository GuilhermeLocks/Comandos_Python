import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="")
cursor = con.cursor()

# Criar o banco de dados se não existir
cursor.execute("CREATE DATABASE IF NOT EXISTS pessoas")
print("Banco de dados 'pessoas' verificado/criado com sucesso!")

# Selecionar o banco de dados
con.database = "pessoas"

# Criar a tabela departamentos
cursor.execute("""
CREATE TABLE IF NOT EXISTS departamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    localizacao VARCHAR(100)
)
""")

print("Tabela 'departamentos' criada com sucesso!")

# Fechar conexão
cursor.close()
con.close()

