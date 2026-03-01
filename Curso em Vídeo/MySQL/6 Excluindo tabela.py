import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='')
cursor = con.cursor()

try:
    database = input('Digite o nome do bando de dados: ')
    tabela = input('Digite a tabela: ')
    cursor.execute(f'use {database}')
    cursor.execute('drop table cursos')
    print(f'\nuse {database}')
    print(f'\ndrop table {tabela};')
    print("\nCursos excluido com sucesso!")
except:
    print("Erro ao deletar cursos")