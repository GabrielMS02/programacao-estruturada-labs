#Escreva um programa que solicite ao usuário para digitar uma frase e substitua todas as ocorrências da letra "a" por "@".

frase = input('Digite uma frase: ')
substring = frase.replace('a', '@')
print(substring)