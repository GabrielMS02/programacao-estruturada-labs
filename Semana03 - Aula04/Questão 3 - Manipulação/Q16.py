#Escreva um programa que peça ao usuário para digitar seu nome completo e imprima apenas o primeiro nome.

nome = input('Digite seu nome completo: ')
separar = nome.split()[0]
print(separar)