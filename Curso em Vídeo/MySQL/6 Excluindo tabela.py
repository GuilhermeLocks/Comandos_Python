import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='', database='naruto')
cursor = con.cursor()

try:
    cursor.execute('drop table if exists pessoas')
    print("Pessoas excluido com sucesso!")
except:
    print("Erro ao deletar ninjas")