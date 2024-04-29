# Criar um laço de repetição que escreva seu nome ao inverso:

nome = input('\nInforme seu nome: ')
nome_inverso = ''

for i in range(len(nome) - 1, -1, -1):
    nome_inverso = nome_inverso + nome[i]

print(f'\nSeu nome ao inverso é {nome_inverso}!')