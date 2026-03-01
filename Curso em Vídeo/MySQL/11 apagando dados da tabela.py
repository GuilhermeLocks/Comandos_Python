import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='')
cursor = con.cursor()

try:
    database = input(f'Digite o nome do bando de dados: ')
    cursor.execute(f'USE {database};')
    table = input(f'Digite o nome da tabela: ')
    cursor.execute(f'TRUNCATE {table};')
    print(f'\nUSE {database};')
    print(f'\nTRUNCATE {table};')
    print("\nDados de cursos excluido com sucesso!")
except:
    print("Erro ao deletar cursos")