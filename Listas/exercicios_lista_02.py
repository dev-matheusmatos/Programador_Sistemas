# 2. Faça um programa, utilizando for e listas / append,
# que peça o nome de três mulheres e três homens e mostre
# na tela três duplas compostas por um homem e uma mulher

print('DUPLAS!')

lista_mulheres = []
lista_homens = []

print()

for i in range(3):
    lista_mulheres.append(input(f'Mulher {i + 1}: '))

print(f'\nMulheres: {lista_mulheres}')

print()

for i in range(3):
    lista_homens.append(input(f'Homem {i + 1}: '))

print(f'\nHomens: {lista_homens}')
print()

for i in range(3):
    print(f'Dupla: {lista_mulheres[i]} e {lista_homens[i]}')