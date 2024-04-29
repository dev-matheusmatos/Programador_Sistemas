# 4 Desenvolver um programa que leia um número não determinado
# de valores, calcule e escreva a média aritmética deles, a quantidade de
# valores positivos, a quantidade de valores negativos,
# o percentual de valores negativos e positivos, qual o valor máximo,
# e qual o valor mínimo

positivos = 0
negativos = 0
somatorio = 0
maior = 0
menor = 0

print()
while True:

    numero = float(input(f'Informe um número ou digite 0 para encerrar: '))
    somatorio += numero

    if numero == 0:
        break

    if numero > 0:
        positivos += 1

    else:
        negativos += 1

    if numero > maior or positivos + negativos == 1:
        maior = numero

    if numero < menor or positivos + negativos == 1:
        menor = numero


print(f'\nA média dos valores informados é de {somatorio / (positivos + negativos):.2f}!')
print(f'A quantidade de valores positivos é de {positivos}!')
print(f'A quantidade de valores negativos é de {negativos}!')
print(f'O percentual de positivos é de {positivos / (positivos + negativos):.2%}!')
print(f'O percentual de negativos é de {negativos / (positivos + negativos):.2%}!')
print(f'O valor máximo foi de {maior:.2f}!')
print(f'O valor mínimo foi de {menor:.2f}!')


