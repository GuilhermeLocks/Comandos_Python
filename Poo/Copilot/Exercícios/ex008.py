class Endereco:
    def __init__(self, rua, cidade, estado):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado

class Cliente(Endereco):
    def __init__(self, nome, endereco, rua, cidade, estado):
        super().__init__(rua, cidade, estado)
        self.nome = nome
        self.endereco = endereco

    def mostrar_dados(self):
        print(f"{self.nome} mora em {self.rua}, {self.cidade} - {self.estado}")

c = Cliente("{nome}", '{endereco}', "{rua}", "{cidade}", "{estado}")
c.mostrar_dados()