def funcao(text):
    print('-'*(len(text)+4))
    print('  {}'.format(text))
    print('-' * (len(text) + 4))
dicionario =  {
'nome':'Gustavo Granabara',
'curso': 'Curso de Python no Youtube',
}
funcao(dicionario['nome'])
funcao(dicionario['curso'])