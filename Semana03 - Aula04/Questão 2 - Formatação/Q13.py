#Escreva um programa que solicite ao usuário um número decimal e imprima uma mensagem formatada mostrando o número com duas casas decimais.

numero = float(input('Insira um número decimal '))
numero_str = str(numero)
numero_str.split('.')

parte0 = numero_str.split('.')[0]
parte1 = numero_str.split('.')[1]


print(parte0 + '.' + parte1[0:2] )