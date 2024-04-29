# 3. Criar um algoritmo quantos números você desejar (laço infinito),
# e ao final dele mostre:

# A lista em ordem crescente
# A lista em ordem decrescente
# A soma de todos os itens
# A média de todos os números

lista_numeros = []
print()

while True:
    numero = int(input('Digite um número ou 0 para sair: '))

    if numero == 0:
        break

    lista_numeros.append(numero)

print()
lista_numeros.sort()
print(f'Ordem crescente: {lista_numeros}')
lista_numeros.sort(reverse=True)
print(f'Ordem decrescente: {lista_numeros}')
print(f'Soma dos números: {sum(lista_numeros)}')
print(f'Média dos números: {sum(lista_numeros) / len(lista_numeros)}')
