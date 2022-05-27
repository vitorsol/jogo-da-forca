def recebe_letra(palavra, letras):
    letra_get = str(input('Digite uma letra: '))

    for c in range(len(palavra)):
        if letra_get == palavra[c]:
            letras[c] = letra_get
    return letras


def forca(erros):
    if erros == 1:
        print('(|)')
    if erros == 2:
        print('(|)\n'
              ' |\n'
              ' |')
    if erros == 3:
        print('(|)\n'
              '\|\n'
              ' |')
    if erros == 4:
        print('(|)\n'
              '\|/\n'
              ' |')
    if erros == 5:
        print('(|)\n'
              '\|/\n'
              ' |\n'
              '/')
    if erros == 6:
        print('(|)\n'
              '\|/\n'
              ' |\n'
              '/ \ ')


def confere(palavra, letras):
    if not recebe_letra(palavra, letras):
        return False
    return True
