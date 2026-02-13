import mysql.connector

database = input('Digite o banco de dados: ')
con = mysql.connector.connect(user='root', password='', host='localhost', database=database)
cursor = con.cursor()
tabela = input('Digite o nome da tabela: ')
onde = input('Digite o id: ')

try:
    cursor.execute(f"SELECT * FROM {tabela};")
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.execute(f'''delete from pessoa
                   where id = '{onde}'
                   limit 1;''')

    cursor.execute(f"SELECT * FROM {tabela};")
    result = cursor.fetchall()
    for row in result:
        print(row)

    # 4. Fechar conexões
    cursor.close()

except  Exception as erro:
    print(f'Erro: {erro}')
