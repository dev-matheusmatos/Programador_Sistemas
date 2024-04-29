# 1. Faça um programa, utilizando for e listas, que pergunte ao
# usuário quantos produtos ele deseja cadastrar, cadastre os produtos
# e seus respectivos preços em listas separadas e os mostre na tela
# juntos.

lista_produtos = []
lista_precos = []

print('CADASTRO DE PRODUTOS!')

qnt_produtos = int(input('''\nQuantos produtos você deseja cadastrar?
Resposta: '''))
print(f'\n{"=" * 50}')

for i in range(qnt_produtos):
    produto = input(f'\nProduto {i + 1}: ')
    lista_produtos.append(produto)
    preco = float(input('Preço: R$ '))
    lista_precos.append(preco)

print(f'\n{"=" * 50}')
print()

for i in range(len(lista_produtos)):
    print(f'Produto: {lista_produtos[i]} - Preço: R$ {lista_precos[i]:.2f}')