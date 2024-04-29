# 9 Faça um programa que implemente um menu onde o usuário
# deverá selecionar 1 ou 0. Caso seja informado um número diferente,
# o programa deverá solicitar uma nova opção.

while True:

    print(f'\n{"=" * 24}')
    print(f'{" " * 10}MENU{" " * 10}')
    print(f'{"=" * 24}')

    opcao = input('''\nEscolha uma opção: 
                  
[1]
[2]
''')

    if opcao == '1':
        break

    elif opcao == '2':
        break
