import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='', database='naruto')
cursor = con.cursor()

try:
    # tabela = input('Digite o nome da tabela: ')
    tabela = 'pessoa'

    cursor.execute(f'''SELECT * FROM {tabela}
                   order by nome desc;''')

    result = cursor.fetchall()
    for row in result:
        print(row)
    print(' ')

    cursor.execute(f'''SELECT nome, id, altura FROM {tabela}
                       order by nome desc;''')

    # 3. Buscar e imprimir dados
    result = cursor.fetchall()
    for row in result:
        print(row)
    print(' ')

    cursor.execute(f'''SELECT nome FROM {tabela}
                            where altura = '1.80'
                           order by nome desc;''')

    result = cursor.fetchall()
    for row in result:
        print(row)

    print(' ')

    cursor.execute(f'''SELECT id, nome FROM {tabela}
                                where id between 1 and 6
                               order by id desc;''')

    result = cursor.fetchall()
    for row in result:
        print(row)

    print(' ')

    cursor.execute(f'''SELECT id, nome FROM {tabela}
                                    where id in (1, 2, 3)
                                   order by id desc;''')

    result = cursor.fetchall()
    for row in result:
        print(row)

    print(' ')

    cursor.execute(f'''SELECT id, nome FROM {tabela}
                                        where id > 5 and id < 9
                                       order by id desc;''')

    result = cursor.fetchall()
    for row in result:
        print(row)

except Exception as erro:
    print(f'Erro: {erro}')
