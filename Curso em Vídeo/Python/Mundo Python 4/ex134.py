from abc import ABC, abstractmethod

class Funcionaria(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < self._salario:
            print('O salario nao pode ser diminuido')
        else:
            self._salario = valor
            self.bonus = (self._salario / 100) * 15
            salario = self._salario
            salario_com_bonus = self._salario + self.bonus
            print(f'{self.nome} ganha R${salario:.2f} o bônus será de R${salario_com_bonus:.2f}')

class Gerente(Funcionaria):

    def calcular_bonus(self):
        self.bonus = (self._salario / 100) * 15
        return f'R${self.bonus:.2f}'

    def __str__(self):
        salario = self._salario
        bonus = self.bonus
        return f'{self.nome} por ser Gerente ganha R${salario:.2f} o bônus será de R${bonus:.2f}'

class Designer(Funcionaria):

    def calcular_bonus(self):
        self.bonus = (self._salario / 100) * 5
        return f'R${self.bonus:.2f}'

    def __str__(self):
        salario = self._salario
        bonus = self.bonus
        return f'{self.nome} por ser Designer ganha R${salario:.2f} o bônus será de R${bonus:.2f}'


class Desenvolvedor(Funcionaria):

    def calcular_bonus(self):
        self.bonus = (self._salario / 100) * 5
        return f'R${self.bonus:.2f}'

    def __str__(self):
        salario = self._salario
        bonus = self.bonus
        return f'{self.nome} por ser Desenvolvedor ganha R${salario:.2f} o bônus será de R${bonus:.2f}'


f1 = Gerente('Fabio', 1000)
print(f1, f1.calcular_bonus())
print()

f1 = Designer('Pedro', 1000)
print(f1, f1.calcular_bonus())
print()

f1 = Desenvolvedor('Paulo', 1000)
print(f1, f1.calcular_bonus())
print()

f1.salario = 100
f1.salario = 10000

