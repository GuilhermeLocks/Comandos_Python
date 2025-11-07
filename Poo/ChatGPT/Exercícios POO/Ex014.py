class Usuario:
    def __init__(self, nome):
        self.nome = nome  # usa o setter automaticamente

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if len(valor) >= 3:
            self._nome = valor
        else:
            raise ValueError("Nome curto demais. O nome deve ter pelo menos 3 caracteres.")


try:
    u = Usuario("Leo")
    print(u.nome)

    u.nome = "Li"  # vai gerar erro
except ValueError as e:
    print("Erro:", e)
