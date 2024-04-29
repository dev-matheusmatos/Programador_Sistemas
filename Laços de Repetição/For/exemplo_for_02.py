# criar um programa que calcule o fatorial

numero = int(input('\nInforme um número: '))
fatorial = 1

for i in range(2, numero + 1):
    fatorial *= i

print(f'\nO fatorial do número informado é {fatorial}!')

from math import factorial

numero = int(input('\nInforme um número inteiro: '))

print(f'\nO fatorial do número informado é {factorial(numero)}')