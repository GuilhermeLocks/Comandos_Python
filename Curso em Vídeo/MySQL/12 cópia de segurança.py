import subprocess
import os

# --- CONFIGURAÇÕES ---
# Verifique se a sua versão é 8.0, 5.7, etc., e ajuste o caminho abaixo se necessário
caminho_mysqldump = r"C:\wamp64\bin\mysql\mysql8.4.7\bin\mysqldump.exe"

host = "localhost"
usuario = "root"
senha = ""  # Se não tiver senha, deixe vazio, mas o -p ainda é necessário
banco = "naruto"
caminho_saida = r"I:\backup_naruto.sql"

# Comando com o caminho completo entre aspas (importante para caminhos com espaços)
comando = f'"{caminho_mysqldump}" -h {host} -u {usuario} -p{senha} {banco} > "{caminho_saida}"'

try:
    subprocess.run(comando, shell=True, check=True)
    print(f"Sucesso! Backup salvo em: {caminho_saida}")
except subprocess.CalledProcessError as e:
    print(f"Erro ao gerar o dump: {e}")

