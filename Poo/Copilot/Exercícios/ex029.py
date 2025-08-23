class reserva:
    def __init__(self, cliente, data):
        self.cliente = cliente
        self.data = data

class reserva_hotel(reserva):
    def tipo(self):
        return 'hotel'

class reserva_voo(reserva):
    def tipo(self):
        return 'voo'

r1 = reserva_hotel("Paulo", "15/08/2025")
r2 = reserva_voo("Ana", "16/08/2025")
print(f"{r1.cliente} - {r1.tipo()} em {r1.data}")
print(f"{r2.cliente} - {r2.tipo()} em {r2.data}")
