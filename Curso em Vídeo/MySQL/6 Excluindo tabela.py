import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='')
cursor = con.cursor()

try:
    database = 'cadastro'
    tabela = input('Digite a tabela: ')
    cursor.execute(f'use {database}')
    cursor.execute(f'drop table {tabela}')
    print(f'\nuse {database}')
    print(f'\ndrop table {tabela};')
    print("\nCursos excluido com sucesso!")
except Exception as erro:
    print(f"Erro: {erro}")