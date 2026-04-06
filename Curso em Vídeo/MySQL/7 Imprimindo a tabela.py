import mysql.connector
# 1. Configurar a conexão
database = 'cadastro'
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=database)

# 2. Criar cursor e executar select


tabela = input('Digite o nome da tabela: ')
print(f'\nUSE {database}')
cursor = db_connection.cursor()
cursor.execute(f"SELECT * FROM {tabela};")
print(f'\nSELECT * FROM {tabela};\n')


# 3. Buscar e imprimir dados
result = cursor.fetchall()
for row in result:
    print(row)

# 4. Fechar conexões
cursor.close()
db_connection.close()
