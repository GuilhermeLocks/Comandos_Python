class veiculo:
    def __inint__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f'{self.marca} {self.modelo} está acelerando')

    def frear(self):
        print(f'{self.marca} {self.modelo} está freando')

class carro(veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas
        self.ligado = False

    def ligar(self):
        if not self.ligar:
            self.ligado = True
            print(f'{self.marca} {self.modelo} lagado.')
        else:
            print(f'{self.marca} {self.modelo} já está ligado')

    def desligado(self):
        if self.ligado:
            self.ligado = False
            print(f'{self.marca} {self.modelo} desligado.')
        else:
            print(f'{self.marca} {self.modelo} já está desligado')

    def acelerar(self):
        if self.ligado:
            super().acelerar()
            print('O carro está em movimento!')
        else:
            print(f'{self.marca} {self.modelo} precisa ser ligado primeiro')

