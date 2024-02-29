#screva um programa que solicite ao usuário uma frase e imprima uma mensagem formatada mostrando a quantidade de caracteres, palavras e linhas na frase.

frase = input('Digite uma frase: ')
linhas = frase.count('\n') + 1
palavras = frase.count(' ') + 1
caracteres = len(frase) - frase.count(' ')
resultado = caracteres, + palavras, + linhas
print(resultado)

