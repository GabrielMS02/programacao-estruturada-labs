#Escreva um programa que solicite ao usuário seu nome completo e imprima as iniciais de cada palavra em letras maiúsculas. Por exemplo, se o nome for "Fulano de Tal", o programa deve imprimir "F.D.T."

nome_completo = input('Digite seu nome completo: ')

#Separar o texto nos espaços
partes_nome = nome_completo.split()

primeiro_nome = partes_nome[0]
segundo_nome = partes_nome[1]
terceiro_nome = partes_nome[2]

inicial1 = primeiro_nome[0:1]
inicial2 = segundo_nome[0:1]
inicial3 = terceiro_nome[0:1]

iniciais = inicial1 + ',' + inicial2 + ',' + inicial3
print(iniciais)
