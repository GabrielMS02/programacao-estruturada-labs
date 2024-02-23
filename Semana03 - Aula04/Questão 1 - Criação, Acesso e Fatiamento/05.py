#Escreva um programa que verifique se uma palavra é um palíndromo (lê-se igual de trás para frente). Exemplo: "radar".

palavra = input('Escreva uma palavra ')
minuscula = palavra.lower()
palavra_invertida = minuscula[::-1]




if palavra_invertida == minuscula:
    print('É palíndromo')

else:
    print('Não é palíndromo')    
