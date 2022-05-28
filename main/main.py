from functions import forca

print('*' * 10, 'Jogo da Forca', '*' * 10)

palavra = ['t', 'e', 's', 't', 'e']
letras = ['_' for letra in palavra]
erros = 0
letras_erradas = []

print('\n', letras, '\n')

while erros < 7:
    print('*' * 35)
    letra_get = str(input('\n->: '))

    if len(letra_get) == 1:
        for c in range(len(palavra)):
            if letra_get == palavra[c]:
                letras[c] = letra_get
        if letra_get not in palavra:
            erros += 1
            letras_erradas.append(letra_get)
    else:
        print('\nERRO: Digite apenas uma letra ou número!\n')

    print('\n', letras, '\n')
    forca(erros)
    print('\n', letras_erradas, '\n')
    if erros == 6:
        print('GAME OVER')
        break
