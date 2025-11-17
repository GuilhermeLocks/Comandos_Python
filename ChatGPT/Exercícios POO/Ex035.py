class Conexao:
    ativas = 0

    def __init__(self):
        Conexao.ativas += 1
        print(f"1Conexões ativas: {Conexao.ativas}")

    def __del__(self):
        Conexao.ativas -= 1
        print(f"2Conexões ativas: {Conexao.ativas}")

c1 = Conexao()
c2 = Conexao()
del c1
