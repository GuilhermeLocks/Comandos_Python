class funcionario:
    def __init__(self, nome, dias_trabalhados):
        self.nome = nome
        self.dias_trabalhados = dias_trabalhados

class clt(funcionario):
    def __init__(self, nome, dias_trabalhados):
        super().__init__(nome, dias_trabalhados)

    def ferias(self):
        self.ferias = 0
        while self.dias_trabalhados - 30 >= 0:
            if self.dias_trabalhados - 30 >= 0:
                self.ferias += 10
                self.dias_trabalhados -= 30
        print(f'{self.nome} é CLT é tem direitos a ferias de {self.ferias} dias')

class pj(funcionario):
    def __init__(self, nome, dias_trabalhados):
        super().__init__(nome, dias_trabalhados)

    def ferias(self):
        print(f'{self.nome} é PJ é nâo tem direitos a ferias')

pj('nome1', 50).ferias()
clt('nome2', 90).ferias()