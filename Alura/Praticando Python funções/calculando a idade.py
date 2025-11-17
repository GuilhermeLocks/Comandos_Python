def ano_de_nascimento(a):
    def ano_atual(b):
        return b-a
    return ano_atual

nascimento = ano_de_nascimento(2000)
atual = nascimento(2025)
print(atual)