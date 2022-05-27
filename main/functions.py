def recebe_letra(palavra, letras):
    acerto = False
    while not acerto:
        letra_get = str(input('Digite uma letra: '))

        for c in range(len(palavra)):
            if letra_get == palavra[c]:
                letras[c] = letra_get
                acerto = True
    return letras
