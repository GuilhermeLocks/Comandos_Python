class evento:
    def __init__(self, titulo, data):
        self.titulo = titulo
        self.data = data

class show(evento):

    def __init__(self, titulo, data):
        super().__init__(titulo, data)

    def dias_para_evento(self):
        print(f'Hoje e dia 7 e o show do {self.titulo} e dia {self.data} e falta {self.data - 7}')

class palestrante(evento):

    def __init__(self, titulo, data):
        super().__init__(titulo, data)

    def dias_para_evento(self):
        print(f'Hoje e dia 7 e o palestra do {self.titulo} e dia {self.data} e falta {self.data - 7}')

show('nome:show', 25).dias_para_evento()
palestrante('nome:Palestrante', 35).dias_para_evento()


