from functions import *

print('*' * 10, 'Jogo da Forca', '*' * 10)

palavra = ['t', 'e', 's', 't', 'e']
letras = ['_' for letra in palavra]
erros = 0

while erros < 6:
    print(recebe_letra(palavra, letras))
    if not confere(palavra, letras):
        erros += 1
    print(erros)
