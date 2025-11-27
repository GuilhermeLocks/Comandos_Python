def cabecalho(text):
    espaco = int(len(text)+12)
    print('-'*espaco)
    print(f'{text:^{espaco}}')
    print('-'*espaco)

cabecalho('texto sem criatividade')
cabecalho('outro texto sem criatividade')