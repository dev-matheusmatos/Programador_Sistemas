lista_notas = []

print('Boletim do Aluno')

for i in range(4):
    nota = float(input(f'Nota {i + 1}: '))
    lista_notas.append(nota)

print(f'Média: {sum(lista_notas) / len(lista_notas)}')


