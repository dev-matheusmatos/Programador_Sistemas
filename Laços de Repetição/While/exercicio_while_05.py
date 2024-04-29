# 5 Crie um programa que simule as operações básicas de um
# banco: Todas as opções devem funcionar. A conta só é acessada caso seja
# apresentada a senha correta.
# Inicialmente devem ser Solicitado informado nº da Conta e Senha;
# Caso a conta e senha estejam corretos,
# redireciona para o seguinte menu:
#
# a. Consultar saldo
# b. Pagar conta
# c. Depositar na conta
# d. Saque
# e. Sair
#
# O programa só deve se encerrar quando for selecionada  a opção SAIR.

import random

cadastro_01 = ''
senha_cadastro_01 = ''
nome = ''
sobrenome = ''
saldo = 0


while True:

    print(f'\n{"="*36}')
    print(f'{' '*10}Banco Desgraçado{' '*10}')
    print(f'{"="*36}')

    opcao_01 = input('''\nSelecione:
    
    [1] ENTRAR
    [2] CADASTRAR NOVA CONTA
    [3] Sair 
    
    ''')

    if opcao_01 == '1':

        conta = input('\nInforme o número da conta: ')
        senha = input('Informe a senha: ')

        if conta == cadastro_01 and senha == senha_cadastro_01:

            while True:

                print(f'{"="*50}')
                print(f'\nSeja bem-vindo, {nome} {sobrenome}!')

                opcao_02 = input('''\nSelecione:
    
                [1] Consultar Saldo
                [2] Pagar conta
                [3] Depositar 
                [4] Saque
                [5] SAIR 
                
                ''')

                print()

                if opcao_02 == '1':

                    print(f'O seu saldo atual é de R$ {saldo:.2f}')

                elif opcao_02 == '2':

                    valor_conta = float(input('Informe o valor da conta em R$: '))

                    if valor_conta <= saldo:

                        saldo -= valor_conta

                        print(f'\nA conta no valor de {valor_conta:.2f} foi paga com sucesso, e seu saldo restante é de R$ {saldo:.2f}')

                    else:

                        print('\nNão há saldo suficiente para pagar a conta informada!')

                elif opcao_02 == '3':

                    saldo += float(input('Informe o valor do depósito em R$: '))
                    print('\nValor depositado com sucesso!')

                elif opcao_02 == '4':

                    saque = float(input('Informe o valor que deseja sacar em R$: '))

                    if saque <= saldo:

                        saldo -= saque

                        print(f'\nO valor de R$ {saque:.2f} foi sacado com sucesso. Seu saldo restante é de R$ {saldo:.2f}!')

                    else:

                        print('\nSaldo insuficiente!')

                elif opcao_02 == '5':
                    break

                else:

                    print('Escolha uma opção válida!')

        else:

            print('\nCadastro Inválido, verifique sua conta e a senha!')

    elif opcao_01 == '2':

        print('\nBem vindo a tela de cadastro de novo usuário!')
        nome = input('\nInforme seu nome: ')
        sobrenome = input('Informe seu sobrenome: ')
        senha_cadastro_01 = input('Informe sua senha: ')

        for i in range(1, 7):

            cadastro_01 += str(random.randint(0, 9))

        print(f'\nO número da sua nova conta cadastrada é {cadastro_01}!')

    elif opcao_01 == '3':
        break

    else:
        print('\nInforme uma opção válida!')

