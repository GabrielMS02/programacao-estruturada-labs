#Escreva um programa que solicite ao usuário para digitar uma frase e verifique se todas as palavras estão em letras maiúsculas.

frase = input('Digite uma frase: ')
frase_maiuscula = frase.upper()

if frase == frase_maiuscula:
    print('Está tudo maiúsculo')

else:
    print('Não está tudo maiúsculo')    

