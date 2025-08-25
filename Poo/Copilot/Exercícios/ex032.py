class tarefa:
    def __init__(self, titulo, status):
        self.titulo = titulo
        self.status = status
        print(f'Tarefa {self.titulo} {self.status}')

    def concluir(self):
        self.status = 'Concluido'
        print(f'Tarefa {self.titulo} {self.status}')

tarefa('Profissional', 'Em andamento').concluir()
tarefa('Pessoal', 'Em andamento').concluir()