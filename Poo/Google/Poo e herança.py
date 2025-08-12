# Classe base Veiculo
class Veiculo:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.marca} {self.modelo} ligado.")
        else:
            print(f"{self.marca} {self.modelo} já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"{self.marca} {self.modelo} desligado.")
        else:
            print(f"{self.marca} {self.modelo} já está desligado.")

    def __str__(self):
        return f"Veículo: {self.marca} {self.modelo}, Cor: {self.cor}, Ligado: {self.ligado}"

# Classe derivada Carro (herda de Veiculo)
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, num_portas):
        super().__init__(marca, modelo, cor)
        self.num_portas = num_portas
        self.velocidade = 0

    def acelerar(self, incremento):
        if self.ligado:
            self.velocidade += incremento
            print(f"Acelerando {self.marca} {self.modelo}. Velocidade atual: {self.velocidade} km/h")
        else:
            print(f"{self.marca} {self.modelo} precisa estar ligado para acelerar.")

    def frear(self, decremento):
        if self.ligado:
            self.velocidade = max(0, self.velocidade - decremento)
            print(f"Freando {self.marca} {self.modelo}. Velocidade atual: {self.velocidade} km/h")
        else:
            print(f"{self.marca} {self.modelo} precisa estar ligado para frear.")

    def __str__(self):
        return f"{super().__str__()} - Portas: {self.num_portas}"

# Classe derivada Moto (herda de Veiculo)
class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, tipo):
        super().__init__(marca, modelo, cor)
        self.tipo = tipo
        self.marcha = 0

    def trocarMarcha(self, nova_marcha):
        if self.ligado:
            self.marcha = nova_marcha
            print(f"Marcha da {self.marca} {self.modelo} alterada para {self.marcha}.")
        else:
            print(f"{self.marca} {self.modelo} precisa estar ligado para trocar de marcha.")

    def __str__(self):
        return f"{super().__str__()} - Tipo: {self.tipo}"

# Exemplo de uso
carro1 = Carro("Toyota", "Corolla", "Prata", 4)
moto1 = Moto("Honda", "CBR 600RR", "Vermelha", "Esportiva")

print(carro1)
print(moto1)

carro1.ligar()
carro1.acelerar(30)
carro1.frear(10)
carro1.desligar()

moto1.ligar()
moto1.trocarMarcha(2)
moto1.desligar()




