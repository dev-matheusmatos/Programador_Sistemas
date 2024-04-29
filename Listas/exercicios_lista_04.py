# Crie um algoritmo que receba quantos nomes (apenas nome) desejar,
# e ao final:

# A lista em ordem crescente
# A lista em ordem decrescente
# O total de nomes cadastrados
# Quantos ‘Carlos’ existem na lista

lista_nomes = []
print()

while True:
    nome = (input('Digite um NOME ou SAIR: '))

    if nome.lower() == 'sair':
        break

    lista_nomes.append(nome)

print()
lista_nomes.sort()
print(f'Ordem crescente: {lista_nomes}')
lista_nomes.sort(reverse=True)
print(f'Ordem decrescente: {lista_nomes}')
print(f'Total de nomes cadastrados: {len(lista_nomes)}')
print(f'Quantos "Carlos" existem: {lista_nomes.count('Carlos')}')
