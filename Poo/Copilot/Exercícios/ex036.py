class animal:
    def __init__(self, nome):
        self.nome = nome

class cachorro(animal):
    def emitir_som(self):
        print(f'O {self.nome} fez au au!')

class gato(animal):
    def emitir_som(self):
        print(f'O {self.nome} fez miau!')

class vaca(animal):
    def emitir_som(self):
        print(f'O {self.nome} fez muuu!')

cachorro('nome').emitir_som()
gato('nome').emitir_som()
vaca('nome').emitir_som()