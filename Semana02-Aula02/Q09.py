#Escreva um programa que solicite ao usuário dois valores booleanos (True ou False) e armazene-os em variáveis. Em seguida, aplique os operadores lógicos "and", "or" e "not" entre essas variáveis e imprima os resultados.

valor1 = int(input('Digite 1 (true) ou 0 (false)'))
valor1_bool = bool(valor1)

valor2 = int(input('Digite 1 (true) ou 0 (false)'))
valor2_bool = bool(valor2)

print('valor1 e valor2', valor1_bool and valor2_bool)
print('valor1 e valor2', valor1_bool or valor2_bool)
print('O valor 1 passando pelo operador NOT retorna: ', not valor1_bool)
print('O valor 2 passando pelo operador NOT retorna: ', not valor2_bool)