nomes = ['Carlos', 'André', 'Getúlio', 'Araci', 'Cleópatra']

indice = int(input('Índice para imprimir: '))

try:
    print(nomes[indice])

except IndexError:
    print('Não encontrado')

finally:
    print('Erro, pc irá explodir em 30 segundos...')

    for i in range(29, 0, -1):
        print(f'{i} segundos...')
        