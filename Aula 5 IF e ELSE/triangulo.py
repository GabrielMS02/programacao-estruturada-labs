A = int(input('Digite o lado A: '))
B = int(input('Digite o lado B: '))
C = int(input('Digite o lado C: '))

if (A < B + C) and  (B < A + C) and (C < A + B):
    if A == B and B == C:
        print('O triângulo é equilátero')
    elif(A != B) and (B != C) and (B != C):
        print('O triângulo é escaleno')
    elif A == B or B == C or C == A:
        print('O triângulo é isosceles')


else:
    print('O triângulo não é válido')



  