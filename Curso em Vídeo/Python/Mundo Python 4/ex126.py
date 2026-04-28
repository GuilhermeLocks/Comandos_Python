from abc import ABC, abstractmethod
class Funcionario(ABC):
    def __init__(self, nome, sel_bruto, salario, sal_min, inss):
        self.nome = nome
        self.sel_bruto = sel_bruto
        self.salario = salario
        self.sal_min = 1612
        self.inss = 7.5

    @abstractmethod
    def cal_sal(self):
        pass

    def analisar_sal(self):
        print(f'Corresponde a {self.salario/self.sal_min:.1f} saláriso mínimos.')

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab, sal_min = 1612):
        self.sal_min = sal_min
        self.nome = nome
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def cal_sal(self):
        self.salario = ((self.valor_hora * self.horas_trab)/100)*92.5
        print(f"O salário de {self.nome} (Funcionario Horista) é de R${self.salario:.2f}")


class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto, salario_min = 1612):
        self.sal_min = salario_min
        self.nome = nome
        self.salario_bruto = salario_bruto

    def cal_sal(self):
        self.salario = (self.salario_bruto/100)*92.5
        print(f"O salário de {self.nome} (Funcionario Horista) é de R${self.salario:.2f}")


f1 = Horista('Paulo', 12, 200)
f1.cal_sal()
f1.analisar_sal()

f2 = Mensalista('Amanda', 9500)
f2.cal_sal()
f2.analisar_sal()