class Endereco:
    def __init__(self, rua, cidade, estado):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado

class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def mostrar_dados(self):
        print(f"{self.nome} mora em {self.endereco.rua}, {self.endereco.cidade} - {self.endereco.estado}")

e = Endereco("Rua A", "Tubarão", "SC")
c = Cliente("Guilherme", e)
c.mostrar_dados()