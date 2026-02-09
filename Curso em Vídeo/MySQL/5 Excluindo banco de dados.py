import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='')
cursor = con.cursor()

try:
    cursor.execute("drop database naruto")
    print("Naruto excluido com sucesso!")
except:
    print("Erro ao deletar naruto")