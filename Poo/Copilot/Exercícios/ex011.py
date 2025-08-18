class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class cliente(pessoa):
    def __init__(self, nome, idade, email):
        super().__init__(nome, idade)
        self.email = email
        cont = 0
        for c in self.email:
            if c == '@':
                cont += 1
        for c in self.email:
            if c == '@':
                if cont == 1:
                    print('O email tem @')
        if cont > 1:
            print(f'O email tem {cont} @')
        if cont == 0:
            print('O email não tem @')
        if self.idade > '18':
            print('A idade e maior que 18')
        elif self.idade == '18':
            print('A idade e iqual a 18')
        else:
            print('A idade e menor que 18')

cliente('nome', '18', 'email@.com')
