def limpar_texto(texto):
    texto = texto.lower()
    caracteres = ",.!|?;:\"'()[]{}"
    for char in caracteres:
        texto = texto.replace(char, '')
    return texto

def contar_palavras(frase, palavra):
    frase_limpa = limpar_texto(frase)
    palavras = frase_limpa.split()
    contador = 0
    for c in palavras:
        if c == palavra:
            contador += 1
    if frase == '':
        frase = '{Vazio}'
    if palavra == '':
        palavra = '{Vazio}'
    return f'Na frase "{frase}", tem a palavra "{palavra}" e aparece {contador} vezes'
