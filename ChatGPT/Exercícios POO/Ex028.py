class Funcionario:
    empresa = "TechCorp"  # atributo de classe

    def __init__(self, nome):
        self.nome = nome

f1 = Funcionario("Ana")
f2 = Funcionario("Bruno")

print(f1.empresa, f2.empresa)
f2.empresa = "OutraEmpresa"
print(f1.empresa, f2.empresa)
