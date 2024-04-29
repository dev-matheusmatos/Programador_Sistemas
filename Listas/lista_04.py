# Quantos nomes começam com vogal?

lista_nomes = ['Bruna', 'Antônia', 'Alice', 'Morgana', 'Orlandina', 'Ellen']

for nome in lista_nomes:
    if nome[-1].upper() in 'AEIOU':
        print(f'{nome} termina com vogal!')

    