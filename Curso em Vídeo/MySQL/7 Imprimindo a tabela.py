import mysql.connector

# 1. Configurar a conexão
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="naruto")

# 2. Criar cursor e executar select
cursor = db_connection.cursor()
tabela = input('Digite o nome da tabela: ')
cursor.execute(f"SELECT * FROM {tabela}")

# 3. Buscar e imprimir dados
result = cursor.fetchall()
for row in result:
    print(row)

# 4. Fechar conexões
cursor.close()
db_connection.close()
