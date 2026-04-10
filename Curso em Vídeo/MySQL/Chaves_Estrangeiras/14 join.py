import mysql.connector
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='cadastro')
# 2. Criar cursor e executar select
tabela = 'pessoas'
print(f'\nUSE cadastro')
cursor = db_connection.cursor()
# cursor.execute(f"SELECT * FROM {tabela};")
cursor.execute(f'use cadastro')
comando = '''
select p.nome, p.curso_preferido 
from pessoas as p left join cursos as c
on p.curso_preferido = c.nome;'''
cursor.execute(comando)
print(comando, '\n')
# 3. Buscar e imprimir dados
result = cursor.fetchall()
for row in result:
    print(row)

# 4. Fechar conexões
cursor.close()
db_connection.close()
