def conversao(texto):
    telefones_int = []
    telefones_com_erro = []

    for c in texto:
        print(type(c), c)
        try:
            telefones_int.append(int(c))
        except ValueError:
            telefones_com_erro.append(c)

    print()

    for c in telefones_int:
        print(type(c), c)

    print()

    for c in telefones_com_erro:
        print(type(c), c)


telefones = ["1198765432p", "21912345678", "31987654321", "11911223344"]
conversao(telefones)