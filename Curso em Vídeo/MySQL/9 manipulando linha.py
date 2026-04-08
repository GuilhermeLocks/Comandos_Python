import mysql.connector

database = 'cadastro'
con = mysql.connector.connect(user='root', password='', host='localhost')
cursor = con.cursor()
tabela = input('Digite o nome da tabela: ')
coluna = input('Digite o nome da coluna: ')
modificacao = input('Digite a alteração da coluna: ')
onde = input('Digite o id: ')

try:
    cursor.execute(f'USE {database}')
    print(f'\nUSE {database}')
    cursor.execute(f"SELECT * FROM {tabela};")
    print(f"\nSELECT * FROM {tabela};\n")
    result = cursor.fetchall()
    for row in result:
        if row[0] == 5:
            print(row)

    cursor.execute(f'''update pessoas
                   set {coluna} = '{modificacao}'
                   where id = '{onde}'
                   limit 1;''')

    print(f'''update pessoas
set {coluna} = '{modificacao}'
where id = '{onde}'
limit 1;''')

    cursor.execute(f"SELECT * FROM {tabela};")
    print(f"\nSELECT * FROM {tabela};\n")
    result = cursor.fetchall()
    for row in result:
        if row[0] == 5:
            print(row)

    # 4. Fechar conexões
    cursor.close()

except  Exception as erro:
    print(f'Erro: {erro}')
