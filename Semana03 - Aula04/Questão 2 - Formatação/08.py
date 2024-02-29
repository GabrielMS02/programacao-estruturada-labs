#Escreva um programa que solicite ao usuário dois números e imprima uma mensagem formatada mostrando a soma, subtração, multiplicação e divisão dos números. Por exemplo: "A soma de {num1} e {num2} é {soma}."

num1 = int(input('Digite um número '))
num2 = int(input('Digite outro número '))

soma = num1 + num2
mensagem = f'A soma é igual a {soma}'
print(mensagem)

subtracao = num1 - num2
mensagem = f'A subtração é igual a {subtracao}'
print(mensagem)

multiplicacao = num1 * num2
mensagem = f'A multiplicação é igual a {multiplicacao}'
print(mensagem)

divisao = num1 / num2
mensagem = f'A divisão é igual a {divisao}'
print(mensagem)
