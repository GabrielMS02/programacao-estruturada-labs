#Escreva um programa que solicite ao usuário a sua idade e verifique se ele é maior de idade (idade igual ou superior a 18 anos). Imprima uma mensagem informando o resultado.

idade = int(input('Digite sua idade '))

if idade >= 18:
    print('É maior de idade')

else:
    print('É menor de idade')