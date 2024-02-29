#Escreva um programa que solicite ao usuário uma palavra e imprima uma mensagem formatada mostrando a palavra em caixa alta e caixa baixa.

palavra = input('Escreva uma palavra: ')
caixa_alta = palavra.upper()
caixa_baixa = palavra.lower()

print(f'Em caixa alta é: {caixa_alta}.', f'Em caixa baixa é: {caixa_baixa}.' )