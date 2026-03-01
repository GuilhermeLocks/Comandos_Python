import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='')
cursor = con.cursor()

try:
    cursor.execute("drop database cadastro")
    print('drop database cadastro;')
    print("\nCadastro excluido com sucesso!")
except:
    print("Erro ao deletar cadastro")