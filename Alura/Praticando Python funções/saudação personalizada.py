def saudacao(texto):
    if texto < 12:
        return 'Bom dia'
    elif 12 <= texto < 18:
        return 'Boa tarde'
    elif 18 <= texto <= 24:
        return 'Boa noite'

print(saudacao(int(input('Digite a hora atual (0-23):'))))