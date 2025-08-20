class transporte:
    def __init__(self, capacidade):
        self.capacidade = capacidade

class onibus(transporte):
    def tipo(self):
        print(f'Tipo de transporte: onibus, capacidade: {self.capacidade}')

class aviao(transporte):
    def tipo(self):
        print(f'Tipo de transporte: aviao, capacidade: {self.capacidade}')

onibus(100).tipo()
aviao(300).tipo()

