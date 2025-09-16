class funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class temporario(funcionario):
    def __init__(self, nome, saldo):
        super().__init__(nome, saldo)

    def calcular_pagamento(self):
        print(f'O {self.nome} com o cargo de temporario tem o salario de {self.salario} com o bonus de 10% firaca com {self.salario*1.1}')

class efetivo(funcionario):
    def __init__(self, nome, saldo):
        super().__init__(nome, saldo)

    def calcular_pagamento(self):
        print(
            f'O {self.nome} com o cargo de efetivo tem o salario de {self.salario} com o bonus de 30% firaca com {self.salario * 1.3}')

class estagiario(funcionario):
    def __init__(self, nome, saldo):
        super().__init__(nome, saldo)

    def calcular_pagamento(self):
        print(
            f'O {self.nome} com o cargo de estagiario tem o salario de {self.salario} com o bonus de 20% firaca com {self.salario * 1.2}')

temporario('nome1', 1000).calcular_pagamento()
estagiario('nome3', 2000).calcular_pagamento()
efetivo('nome2', 3000).calcular_pagamento()

    