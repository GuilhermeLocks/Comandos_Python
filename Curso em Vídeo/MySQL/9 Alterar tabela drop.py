import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='', database='naruto')
cursor = con.cursor()

try:
    cursor.execute('''alter table pessoas
                   drop column prof;''')
    print('Coluna profissão deletada com sucesso!')

except Exception as erro:
    print(f'Erro: [{erro}')