lista_nomes = ['Jonas', 'Isadora', 'Bianca', 'Mauro', 'Jardel']

# print(lista_nomes[2])
#
# for nome in lista_nomes:
#     print(nome)
#
# for indice, nome in enumerate(lista_nomes):
#     print(indice, '-', nome)

# pop apaga o último registro
print(lista_nomes)
lista_nomes.pop()
print(lista_nomes)

# remove remove algum item da lista
lista_nomes.remove('Isadora')
print(lista_nomes)

# pop também apaga por índice
lista_nomes.pop(0)

lista_nomes2 = ['João', 'Delclécio', 'Jairo']
lista_nomes += lista_nomes2
print(lista_nomes)

lista_nomes.insert((len(lista_nomes)), lista_nomes2)
print(lista_nomes)

print(lista_nomes.count('Isadora'))