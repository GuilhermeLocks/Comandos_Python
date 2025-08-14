class animal:
    def falar(self):
        print('Som de animal')

class cachorro(animal):
    def falar(self,):
        print('Au, Au')

class gato(animal):
    def falar(self):
        print('Miau, miau')

animais = [cachorro(),gato()]
for c in animais:
    c.falar()

cachorro().falar()
gato().falar()