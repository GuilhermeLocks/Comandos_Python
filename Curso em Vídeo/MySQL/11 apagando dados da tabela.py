import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='', database='naruto')
cursor = con.cursor()

try:
    cursor.execute('truncate cursos')
    print("Dados de cursos excluido com sucesso!")
except:
    print("Erro ao deletar cursos")