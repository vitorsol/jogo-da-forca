from functions import recebe_letra

palavra = [letra for letra in input('Primeira palavra: ')]
letras = ['_' for letra in palavra]
erros = 0

while erros < 6:
    recebe_letra(palavra, letras)
