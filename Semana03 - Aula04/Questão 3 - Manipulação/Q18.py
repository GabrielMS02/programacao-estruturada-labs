#Escreva um programa que solicite ao usuário para digitar uma frase e verifique se ela termina com um ponto final.

frase = input('Digite uma frase: ')

if frase[-1] == '.' :
    print('Termina com ponto final')

else: 
    print('Não termina com ponto final')    