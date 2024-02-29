#Escreva um programa que solicite ao usuário uma quantidade de horas, minutos e segundos, e imprima uma mensagem formatada mostrando o total de segundos. Por exemplo: "O total de segundos é {total_segundos}."

horas = int(input('Digite uma quantidade de horas '))
minutos = int(input('Digite uma quantidade de minutos '))
segundos = int(input('Digite uma quantidade de segundos '))

total = (horas*60)*60 + minutos*60 + segundos
mensagem = 'O total de segundos é {}'.format(total)
print(mensagem)
