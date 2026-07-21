from rich import inspect

class Retangulo:


    def __init__(self, base = 1, altura = 1):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura


    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            print('TypeError(O valor da base deve ser um número)')
        if valor < 0:
            print('ValueError(Valor inválido para a base)')
        else:
            self._base = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            print('TypeError(O valor da base deve ser um número)')
        if valor < 0:
            print('ValueError(Valor inválido para a base)')
        else:
            self._altura = valor


    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    @area.setter
    def area(self, area):
        print('PermissionError(Área não pode ser configurada desse jeito.)')

    @property
    def medidas(self):
        return f'''Base: {self._base}\nAltura: {self._altura}\nÁrea: {self._base * self._altura}'''

    @medidas.setter
    def medidas(self, medidas: tuple):
        if not isinstance(medidas, tuple):
            print('TypeError(As medidas devem ser infotmadas dentro de uma tupla)')
        if len(medidas) != 2 :
            print('SyntaxError(Informe uma tupla com apenas dois valores númericos)')
        if isinstance(medidas[0], float) or isinstance(medidas[0], int):
            self.base  = medidas[0]
        else:
            print('TypeError(A base deve ser um número)')
        if isinstance(medidas[1], float) or isinstance(medidas[1], int):
            self.altura  = medidas[1]
        else:
            print('TypeError(A altura deve ser um número)')
r= Retangulo()
try:
    r.base = 12
    r.altura = -15
    r.medidas = (3, 9)
except TypeError as e:
    print(f'Erro: {e}')

print(r.medidas)


