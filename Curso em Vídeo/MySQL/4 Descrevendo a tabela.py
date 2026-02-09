import mysql.connector

# Detalhes da sua conexão com o banco de dados
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost', # ou o IP do seu servidor
    'database': 'naruto'
}

try:
    # 1. Conectar ao MySQL
    conn = mysql.connector.connect(**config)
    if conn.is_connected():
        print('Conexão bem-sucedida ao MySQL')

    # 2. Criar um objeto cursor
    cursor = conn.cursor()

    # 3. Executar o comando DESCRIBE para uma tabela específica
    table_name = 'ninjas' # Substitua pelo nome real da tabela
    query = f"DESCRIBE {table_name}"
    cursor.execute(query)

    # 4. Obter e exibir os resultados
    # fetchall() retorna todos os resultados da consulta
    results = cursor.fetchall()

    print(f"\nEstrutura da tabela '{table_name}':")
    print("-" * 55)
    print(f"{'Campo':<20} | {'Tipo':<15} | {'Nulo':<5} | {'Chave':<5}")
    print("-" * 55)
    for row in results:
        # A saída de DESCRIBE geralmente tem 6 colunas: Field, Type, Null, Key, Default, Extra
        field, type_name, null, key, default, extra = row
        print(f"{field:<20} | {type_name!s:<15} | {null:<5} | {key:<5}")
    print("-" * 55)

except mysql.connector.Error as e:
    print(f"Erro ao conectar ou executar a consulta: {e}")

finally:
    # 5. Fechar o cursor e a conexão
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print('Conexão MySQL fechada.')