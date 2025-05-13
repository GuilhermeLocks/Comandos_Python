dados = {}
dados = {'nome':'pedro', 'idade':'25'}
dados['sexo'] = 'M'
print(dados['nome'])
print(dados['idade'])
print(dados['sexo'])
del dados['idade']
print(dados)
print(dados.values())
print(dados.keys())
print(dados.items())
for k, v in dados.items():
    print(k, v) 