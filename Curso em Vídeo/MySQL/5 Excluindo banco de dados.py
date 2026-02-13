import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='')
cursor = con.cursor()

try:
    cursor.execute("drop database cadastro")
    print("Cadastro excluido com sucesso!")
except:
    print("Erro ao deletar cadastro")