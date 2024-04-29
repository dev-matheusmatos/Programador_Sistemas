# Crie um algoritmo que receba valores aleatórios (de qualquer tipo),
# e ao final:
# A lista em ordem inversa ao que foi lançado

lista_valores = []
print()

while True:
    valor = (input('Digite um valor ou SAIR: '))

    if valor.lower() == 'sair':
        break

    lista_valores.append(valor)

print()
lista_valores.reverse()
print(lista_valores)
