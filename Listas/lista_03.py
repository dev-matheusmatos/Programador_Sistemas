# 4 Desenvolver um programa que leia um número não determinado
# de valores, calcule e escreva a média aritmética deles, a quantidade de
# valores positivos, a quantidade de valores negativos,
# o percentual de valores negativos e positivos, qual o valor máximo,
# e qual o valor mínimo

lista = []

while True:

    numero = int(input('Digite um número: '))

    if numero == 0:
        break

    lista.append(numero)

lista.sort()
qt_negativos = 0
for numero in lista:
    if numero < 0:
        qt_negativos += 1
        
print(f'Máximo: {max(lista)}')
print(f'Mínimo: {min(lista)}')
print(f'Média: {sum(lista) / len(lista)}')
print(f'Quantidade de negativos: {qt_negativos}')
print(f'Quantidade de positovos: {len(lista) - qt_negativos}')
print(f'% Negativos: {qt_negativos / len(lista):.2%}')
print(f'% Positivos: {1 - qt_negativos / len(lista):.2%}')



