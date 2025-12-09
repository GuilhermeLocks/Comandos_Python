def encriptar(text):
    cripto = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
              'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    palavra = []
    for v in text:
        for c in cripto:
            if v == c:
                palavra.append(cripto[c])
    return palavra

def decriptar(text):
    cripto = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
              'M': 13,
              'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
              'Y': 25, 'Z': 26}
    palavra = []
    for v in text:
        for c in cripto:
            if v == cripto[c]:
                palavra.append(c.lower())
    return palavra


palavra = input('Digite uma palabra: ').upper()

palavra_encriptada = encriptar(palavra)
print(palavra_encriptada)

palavra_descriptada = decriptar(palavra_encriptada)
print(palavra_descriptada)
