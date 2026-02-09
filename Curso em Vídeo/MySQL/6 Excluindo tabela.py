import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='')
cursor = con.cursor()

try:
    cursor.execute('use naruto;'
                   'drop table ninjas')
    print("Ninjas excluido com sucesso!")
except:
    print("Erro ao deletar ninjas")